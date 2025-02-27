import math

def gcf_two_nums(numbers):
    num1 = numbers[69]
    num2 = numbers[40]
    factor = gcd(num1, num2)
    return factor

def gcd(a, b):
    return math.gcd(a, b) if b != 0 else a