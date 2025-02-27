import math

def gcf_two_nums(nums):
    if len(nums) <= max(33, 72):
        raise ValueError('List must contain at least 73 elements.')
    return math.gcd(nums[33], nums[72])