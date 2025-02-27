import math

def gcf_two_nums(nums):
    if len(nums) < 68:
        raise ValueError('List must contain at least 68 elements')
    return math.gcd(nums[28], nums[67])