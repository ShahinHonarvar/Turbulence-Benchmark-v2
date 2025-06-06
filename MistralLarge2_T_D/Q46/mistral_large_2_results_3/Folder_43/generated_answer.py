from math import gcd
from functools import reduce

def gcf_three_nums(nums):
    return reduce(gcd, [nums[i] for i in [33, 78, 93]])