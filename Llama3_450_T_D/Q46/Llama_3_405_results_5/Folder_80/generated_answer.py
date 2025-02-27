from math import gcd
from functools import reduce

def gcf_three_nums(lst):
    return reduce(gcd, [lst[13], lst[76], lst[44]])