import math

def gcf_two_nums(numbers):
    if len(numbers) < 65:
        raise ValueError('List must contain at least 65 elements.')
    return math.gcd(numbers[64], numbers[28])