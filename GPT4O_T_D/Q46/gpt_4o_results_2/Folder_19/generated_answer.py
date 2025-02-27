import math

def gcf_three_nums(nums):
    if len(nums) < 100:
        return None
    return math.gcd(math.gcd(nums[40], nums[15]), nums[99])