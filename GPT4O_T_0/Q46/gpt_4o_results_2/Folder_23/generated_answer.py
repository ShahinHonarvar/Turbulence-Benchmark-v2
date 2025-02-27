import math

def gcf_three_nums(numbers):
    if len(numbers) < 81:
        raise ValueError('List must contain at least 81 elements.')
    return math.gcd(math.gcd(numbers[31], numbers[25]), numbers[80])