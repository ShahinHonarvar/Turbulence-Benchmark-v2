from math import gcd
from functools import reduce

def gcf_three_nums(nums):
    target_indices = [74, 60, 28]
    elements = [nums[i] for i in target_indices]
    return reduce(gcd, elements)