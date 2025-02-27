import math

def gcf_two_nums(numbers):
    if len(numbers) < 308:
        raise ValueError('List must contain at least 308 elements')
    return math.gcd(numbers[184], numbers[307])