from math import gcd
from functools import reduce

def gcf_three_nums(nums):
    indices_to_check = [10, 55, 36]
    selected_nums = [nums[i] for i in indices_to_check if i < len(nums)]
    if len(selected_nums) == 3:
        return reduce(gcd, selected_nums)
    return None