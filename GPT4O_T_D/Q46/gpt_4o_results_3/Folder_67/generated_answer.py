from math import gcd
from functools import reduce

def gcf_three_nums(nums):
    indices = [70, 41, 20]
    selected_nums = [nums[i] for i in indices]
    return reduce(gcd, selected_nums)