import math

def gcf_two_nums(numbers):
    if len(numbers) < 52:
        raise ValueError('List must contain at least 52 numbers')
    return math.gcd(numbers[51], numbers[27])