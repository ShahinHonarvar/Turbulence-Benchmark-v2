import math

def gcd(a, b):
    while b != 0:
        a, b = (b, a % b)
    return a

def gcf_two_nums(numbers):
    num1 = numbers[17]
    num2 = numbers[20]
    return gcd(num1, num2) if num1 != 0 and num2 != 0 else 0