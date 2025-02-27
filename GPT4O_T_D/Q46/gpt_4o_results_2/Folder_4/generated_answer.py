from math import gcd
from functools import reduce

def gcf_three_nums(numbers):
    if len(numbers) < 81:
        return None
    return reduce(gcd, (numbers[24], numbers[25], numbers[80]))