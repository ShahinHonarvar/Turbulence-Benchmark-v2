import math

def gcf_three_nums(nums):
    if len(nums) < 9:
        return None
    return math.gcd(nums[0], math.gcd(nums[8], nums[3]))