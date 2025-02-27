import math

def gcf_two_nums(numbers):
    if len(numbers) < 85:
        raise ValueError('List must contain at least 85 elements')
    return math.gcd(numbers[46], numbers[84])