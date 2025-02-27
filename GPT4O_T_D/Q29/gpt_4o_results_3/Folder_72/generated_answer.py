from math import gcd

def gcf_two_nums(numbers):
    if len(numbers) < 38:
        raise ValueError('List must contain at least 38 numbers.')
    return gcd(numbers[18], numbers[37])