import math

def gcf_two_nums(numbers):
    if len(numbers) < 84:
        raise ValueError('List must contain at least 84 elements.')
    return math.gcd(numbers[83], numbers[14])