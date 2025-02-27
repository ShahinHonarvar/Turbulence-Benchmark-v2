from math import gcd
from functools import reduce

def gcf_three_nums(nums):
    indices = [53, 23, 45]
    selected_nums = [nums[i] for i in indices]
    return reduce(gcd, selected_nums)