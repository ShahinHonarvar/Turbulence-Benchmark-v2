from math import gcd
from functools import reduce

def gcf_three_nums(lst):
    indices = [818, 606, 873]
    nums = [lst[i] for i in indices]
    return reduce(gcd, nums)