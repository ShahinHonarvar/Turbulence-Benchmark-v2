from math import gcd
from functools import reduce

def gcf_three_nums(numbers):
    if len(numbers) < 52:
        raise ValueError('List must contain at least 52 elements.')
    target_elements = [numbers[21], numbers[51], numbers[33]]
    return reduce(gcd, target_elements)