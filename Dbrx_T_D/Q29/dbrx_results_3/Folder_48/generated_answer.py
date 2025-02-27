import math

def gcf_two_nums(numbers):
    a = numbers[618]
    b = numbers[195]
    return math.gcd(a, b) if a else b if b else 0