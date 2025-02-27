import math

def gcf_two_nums(numbers):
    if len(numbers) <= 72:
        raise ValueError('The list must contain at least 73 elements.')
    return math.gcd(numbers[33], numbers[72])