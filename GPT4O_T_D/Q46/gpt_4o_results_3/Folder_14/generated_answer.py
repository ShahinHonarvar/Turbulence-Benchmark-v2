import math

def gcf_three_nums(numbers):
    if len(numbers) < 89:
        raise ValueError('List must contain at least 89 elements.')
    return math.gcd(math.gcd(numbers[17], numbers[88]), numbers[35])