import math

def gcf_two_nums(nums):
    if len(nums) <= 83:
        raise ValueError('List must contain at least 84 elements')
    return math.gcd(nums[20], nums[83])