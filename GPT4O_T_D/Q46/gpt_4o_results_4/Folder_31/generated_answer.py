import math

def gcf_three_nums(nums):
    if len(nums) <= max(90, 54, 96):
        raise ValueError('List must have at least 97 elements')
    return math.gcd(math.gcd(nums[90], nums[54]), nums[96])