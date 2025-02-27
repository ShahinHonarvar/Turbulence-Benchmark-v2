from math import gcd
    from functools import reduce

def gcf_three_nums(lst):
    nums = [lst[13], lst[76], lst[44]]
    return reduce(gcd, nums)