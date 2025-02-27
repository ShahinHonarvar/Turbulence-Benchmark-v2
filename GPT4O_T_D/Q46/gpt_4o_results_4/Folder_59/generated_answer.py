from math import gcd
from functools import reduce

def gcf_three_nums(lst):
    if len(lst) < 9:
        raise ValueError('List must contain at least 9 elements.')
    return reduce(gcd, (lst[7], lst[6], lst[8]))