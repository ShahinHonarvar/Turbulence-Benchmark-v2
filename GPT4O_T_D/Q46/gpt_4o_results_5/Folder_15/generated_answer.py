import math

def gcf_three_nums(numbers):
    if len(numbers) < 9:
        raise ValueError('List must contain at least 9 elements.')
    return math.gcd(math.gcd(numbers[4], numbers[0]), numbers[8])