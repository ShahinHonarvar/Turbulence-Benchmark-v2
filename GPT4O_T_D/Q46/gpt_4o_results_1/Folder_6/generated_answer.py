import math

def gcf_three_nums(nums):
    if len(nums) > 94:
        return math.gcd(nums[93], math.gcd(nums[94], nums[57]))
    else:
        return None