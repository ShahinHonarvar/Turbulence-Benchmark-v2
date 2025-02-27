from math import gcd
from functools import reduce

def gcf_three_nums(numbers):
    if len(numbers) < 75:
        raise ValueError('List must contain at least 75 numbers.')
    return reduce(gcd, (numbers[20], numbers[35], numbers[74]))