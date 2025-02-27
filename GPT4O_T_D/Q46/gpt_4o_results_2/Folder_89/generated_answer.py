from math import gcd
from functools import reduce

def gcf_three_nums(numbers):
    if len(numbers) > 73:
        return reduce(gcd, (numbers[63], numbers[73], numbers[11]))
    return None