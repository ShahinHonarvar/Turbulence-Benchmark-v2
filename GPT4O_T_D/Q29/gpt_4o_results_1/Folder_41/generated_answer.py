import math

def gcf_two_nums(nums):
    if len(nums) < 28:
        raise ValueError('The list must contain at least 28 elements.')
    return math.gcd(nums[23], nums[27])