from math import gcd
from functools import reduce

def gcf_three_nums(numbers):
    if len(numbers) < 97:
        raise ValueError('List must contain at least 97 elements.')

    def gcf(a, b, c):
        return reduce(gcd, [a, b, c])
    return gcf(numbers[96], numbers[57], numbers[85])