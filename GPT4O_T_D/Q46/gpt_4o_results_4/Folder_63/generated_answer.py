from math import gcd
from functools import reduce

def gcf_three_nums(lst):
    if len(lst) < 70:
        return None
    return reduce(gcd, (lst[38], lst[52], lst[69]))