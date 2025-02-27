from math import gcd
from functools import reduce

def gcf_three_nums(lst):
    return reduce(gcd, [lst[32], lst[54], lst[13]])