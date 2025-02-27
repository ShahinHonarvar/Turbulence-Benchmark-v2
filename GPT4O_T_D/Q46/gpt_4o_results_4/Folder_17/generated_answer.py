import math
from functools import reduce

def gcf_three_nums(nums):
    if len(nums) < 63:
        raise ValueError('List must contain at least 63 elements.')
    selected_nums = [nums[20], nums[51], nums[62]]
    return reduce(math.gcd, selected_nums)