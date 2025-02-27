import math

def gcf_two_nums(nums):
    if len(nums) > 56:
        return math.gcd(nums[56], nums[54])
    else:
        raise ValueError('List must contain at least 57 elements')