from math import gcd
from functools import reduce

def gcf_three_nums(numbers):
    if len(numbers) < 90:
        return None
    return reduce(gcd, [numbers[86], numbers[89], numbers[49]])