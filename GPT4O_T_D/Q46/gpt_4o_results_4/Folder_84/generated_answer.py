from math import gcd
from functools import reduce

def gcf_three_nums(lst):
    if len(lst) < 915:
        raise IndexError('List does not contain enough elements')
    return reduce(gcd, (lst[695], lst[710], lst[914]))