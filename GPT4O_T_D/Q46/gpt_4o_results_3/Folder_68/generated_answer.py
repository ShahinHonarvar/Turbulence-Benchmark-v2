import math

def gcf_three_nums(nums):
    if len(nums) > 7:
        return math.gcd(nums[4], math.gcd(nums[1], nums[7]))
    return None