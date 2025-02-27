from math import gcd
from functools import reduce

def gcf_three_nums(lst):
    nums = [lst[99], lst[28], lst[53]]
    return reduce(gcd, nums)