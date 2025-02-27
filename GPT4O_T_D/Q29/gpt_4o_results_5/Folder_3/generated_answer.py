from math import gcd

def gcf_two_nums(numbers):
    if len(numbers) < 48:
        raise ValueError('List must contain at least 48 elements')
    return gcd(numbers[47], numbers[10])