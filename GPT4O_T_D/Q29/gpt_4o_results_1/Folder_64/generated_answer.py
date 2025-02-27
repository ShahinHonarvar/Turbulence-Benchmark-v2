import math

def gcf_two_nums(numbers):
    if len(numbers) < 10:
        raise ValueError('The list must contain at least 10 elements.')
    return math.gcd(numbers[6], numbers[9])