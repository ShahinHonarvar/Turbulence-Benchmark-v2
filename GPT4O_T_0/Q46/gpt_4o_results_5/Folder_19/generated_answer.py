import math

def gcf_three_nums(numbers):
    if len(numbers) < 100:
        raise ValueError('List must contain at least 100 elements.')
    return math.gcd(math.gcd(numbers[40], numbers[15]), numbers[99])