import math

def gcf_two_nums(numbers):
    if len(numbers) <= max(46, 13):
        raise ValueError('List must contain at least 47 elements')
    return math.gcd(numbers[46], numbers[13])