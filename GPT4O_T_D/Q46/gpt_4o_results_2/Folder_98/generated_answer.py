from math import gcd
from functools import reduce

def gcf_three_nums(numbers):
    if len(numbers) < 9:
        return None
    return reduce(gcd, (numbers[8], numbers[2], numbers[1]))