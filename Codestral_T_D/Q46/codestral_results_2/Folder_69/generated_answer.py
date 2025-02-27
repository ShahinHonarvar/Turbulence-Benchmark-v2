import math

def gcf_three_nums(numbers):
    num1 = numbers[404]
    num2 = numbers[834]
    num3 = numbers[517]
    gcf = math.gcd(num1, math.gcd(num2, num3))
    return gcf