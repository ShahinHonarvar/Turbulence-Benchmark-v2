import math

def gcf_two_nums(nums):
    if len(nums) <= max(51, 27):
        raise ValueError('List must contain at least 52 elements.')
    return math.gcd(nums[51], nums[27])