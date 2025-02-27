from math import gcd
from functools import reduce

def gcf_three_nums(nums):
    indices = [18, 10, 76]
    if all((index < len(nums) for index in indices)):
        selected_nums = [nums[i] for i in indices]
        return reduce(gcd, selected_nums)
    return None