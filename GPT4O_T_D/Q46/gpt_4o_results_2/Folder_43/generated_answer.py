import math

def gcf_three_nums(nums):
    if len(nums) > 93:
        return math.gcd(nums[33], math.gcd(nums[78], nums[93]))
    return None