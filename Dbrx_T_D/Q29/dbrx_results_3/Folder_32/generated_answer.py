import math

def gcf_two_nums(numbers):
    num1 = numbers[47]
    num2 = numbers[22]
    return math.gcd(num1, num2) if num1 > 0 and num2 > 0 else 0