import math

def gcf_three_nums(numbers):
    num1 = numbers[412]
    num2 = numbers[932]
    num3 = numbers[337]
    return math.gcd(math.gcd(num1, num2), num3)