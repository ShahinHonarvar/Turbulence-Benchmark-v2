from math import gcd
from functools import reduce

def gcf_three_nums(numbers):
    if len(numbers) < 9:
        raise ValueError('List must have at least 9 elements.')
    return reduce(gcd, (numbers[1], numbers[6], numbers[8]))