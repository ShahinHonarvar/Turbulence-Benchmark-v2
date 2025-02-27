from math import gcd
from functools import reduce

def gcf_three_nums(nums):
    if len(nums) < 74:
        return None
    return reduce(gcd, (nums[63], nums[73], nums[11]))