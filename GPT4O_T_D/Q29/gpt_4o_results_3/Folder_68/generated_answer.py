import math

def gcf_two_nums(numbers):
    if len(numbers) < 10:
        raise ValueError('List must contain at least 10 integers.')
    return math.gcd(numbers[8], numbers[9])