from math import gcd
from functools import reduce

def gcf_three_nums(nums):
    indices = [13, 76, 44]
    if all((index < len(nums) for index in indices)):
        selected_nums = [nums[index] for index in indices]
        return reduce(gcd, selected_nums)
    raise ValueError('List does not contain required indices')