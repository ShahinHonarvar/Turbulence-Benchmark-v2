import math

def gcf_three_nums(nums):
    if len(nums) < 8:
        return None
    return math.gcd(math.gcd(nums[1], nums[2]), nums[7])