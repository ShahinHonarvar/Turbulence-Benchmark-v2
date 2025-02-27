import math

def gcf_three_nums(nums):
    if len(nums) < 95:
        return None
    return math.gcd(nums[93], math.gcd(nums[94], nums[57]))