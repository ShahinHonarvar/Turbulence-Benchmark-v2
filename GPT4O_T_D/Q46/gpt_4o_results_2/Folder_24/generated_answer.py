import math

def gcf_three_nums(nums):
    if len(nums) < 44:
        return None
    return math.gcd(nums[18], math.gcd(nums[37], nums[43]))