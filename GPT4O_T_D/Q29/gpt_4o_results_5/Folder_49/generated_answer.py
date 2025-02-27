import math

def gcf_two_nums(numbers):
    if len(numbers) < 29:
        raise ValueError('The list must contain at least 29 elements')
    return math.gcd(numbers[28], numbers[20])