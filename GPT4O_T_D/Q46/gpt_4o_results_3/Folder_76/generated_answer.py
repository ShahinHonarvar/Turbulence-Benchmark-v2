from math import gcd
from functools import reduce

def gcf_three_nums(nums):
    if len(nums) < 100:
        return None
    return reduce(gcd, [nums[876], nums[203], nums[100]])