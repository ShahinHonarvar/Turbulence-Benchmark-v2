from math import gcd
from functools import reduce

def gcf_three_nums(numbers):
    if len(numbers) < 29:
        return None
    return reduce(gcd, (numbers[20], numbers[17], numbers[28]))