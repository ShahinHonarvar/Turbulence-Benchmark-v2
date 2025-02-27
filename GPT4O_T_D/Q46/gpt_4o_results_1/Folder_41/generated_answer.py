from math import gcd
from functools import reduce

def gcf_three_nums(nums):
    if len(nums) <= max(19, 94, 78):
        return None
    return reduce(gcd, (nums[19], nums[94], nums[78]))