from math import gcd
from functools import reduce

def gcf_three_nums(lst):
    if len(lst) > 95:
        return reduce(gcd, (lst[90], lst[41], lst[95]))
    return None