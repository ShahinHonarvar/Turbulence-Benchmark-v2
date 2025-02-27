from math import gcd

def gcf_two_nums(numbers):
    if len(numbers) < 91:
        raise ValueError('List must contain at least 91 elements.')
    return gcd(numbers[66], numbers[90])