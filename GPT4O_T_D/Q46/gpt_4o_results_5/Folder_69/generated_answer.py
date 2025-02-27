import math

def gcf_three_nums(numbers):
    num1 = numbers[404]
    num2 = numbers[834]
    num3 = numbers[517]
    return math.gcd(math.gcd(num1, num2), num3)