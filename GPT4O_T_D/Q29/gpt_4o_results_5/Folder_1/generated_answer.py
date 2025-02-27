import math

def gcf_two_nums(numbers):
    if len(numbers) < 67:
        raise ValueError('The list must contain at least 67 elements.')
    return math.gcd(numbers[13], numbers[66])