import math

def gcf_two_nums(nums):
    if len(nums) < 79:
        raise ValueError('List does not have enough elements.')
    return math.gcd(nums[78], nums[16])