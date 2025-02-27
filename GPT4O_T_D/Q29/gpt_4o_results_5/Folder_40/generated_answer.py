import math

def gcf_two_nums(numbers):
    if len(numbers) <= max(7, 9):
        raise ValueError('List must have at least 10 elements.')
    return math.gcd(numbers[7], numbers[9])