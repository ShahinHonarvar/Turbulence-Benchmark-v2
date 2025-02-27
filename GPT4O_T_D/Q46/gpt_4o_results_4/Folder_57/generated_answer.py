from math import gcd
from functools import reduce

def gcf_three_nums(numbers):
    if len(numbers) > 95:
        return reduce(gcd, (numbers[90], numbers[41], numbers[95]))
    return None