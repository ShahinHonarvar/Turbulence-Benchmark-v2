from math import gcd
from functools import reduce

def gcf_three_nums(lst):
    return reduce(gcd, [lst[10], lst[55], lst[36]])