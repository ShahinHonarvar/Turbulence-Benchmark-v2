from math import gcd
from functools import reduce

def gcf_three_nums(lst):
    if len(lst) < 44:
        return None
    nums = [lst[18], lst[37], lst[43]]
    return reduce(gcd, nums)