import math

def gcf_three_nums(nums):
    if len(nums) < 71:
        return None
    return math.gcd(nums[13], math.gcd(nums[70], nums[32]))