import math

def gcf_two_nums(numbers):
    if len(numbers) <= max(300, 616):
        raise ValueError('The list must contain at least 617 elements.')
    return math.gcd(numbers[300], numbers[616])