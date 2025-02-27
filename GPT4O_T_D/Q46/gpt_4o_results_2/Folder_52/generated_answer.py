from math import gcd
from functools import reduce

def gcf_three_nums(numbers):
    if len(numbers) < 75:
        raise ValueError('List must contain at least 75 elements.')
    return reduce(gcd, (numbers[19], numbers[49], numbers[74]))