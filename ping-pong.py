from pygame import *
'''Необходимые классы'''

class GameSprite(sprite.Sprite):
  # конструктор класса
    def __init__(self, player_image, player_x, player_y, size_x, size_y, player_speed):
        # Вызываем конструктор класса (Sprite):
        sprite.Sprite.__init__(self)

        # каждый спрайт должен хранить свойство image - изображение
        self.image = transform.scale(image.load(player_image), (size_x, size_y))
        self.speed = player_speed

        # каждый спрайт должен хранить свойство rect - прямоугольник, в который он вписан
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
 
  # метод, отрисовывающий героя на окне
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
  def update_r(self):
    keys = key.get_pressed()
    if keys[K_UP] and self.rect.y > 5:
      self.rect.y -= self.speed
    if keys[K_DOWN] and self.rect.y < win_height - 80:
      self.rect.y += self.speed
  def update_l(self):
    keys = key.get_pressed()
    if keys[K_w] and self.rect.y > 5:
      self.rect.y -= self.speed
    if keys[K_s] and self.rect.y < win_height - 80:
      self.rect.y += self.speed

#игровая сцена
ифсл - (200.255.255)
win_width = 600
win_hight = 600
window = deisplay.set_mode((win_width, win_hight))
window.fill(back)

#флаги, отвечающие за состояние игры
game = true
finish = False
clock = time.Clock()
FPS = 60

#создание ракетки и мяча
racket1 = Player('racket.png', 30, 200, 4, 50, 150)
racket2 = Player('racket.png', 520, 200, 4, 50,150)
ball = GameSprite('tennis_ball.png'200,2004,50,50)



font.init()
font = font.Font(None,35)
lose1 = font.render('PLAYER 1 LOSE!', True, (180,0,0))
lose2 = font.render('PLAYER 2 LOSE!', True, (180,0,0))

speed_x = 3
speed_y = 3
