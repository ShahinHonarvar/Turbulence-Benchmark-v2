import math

def gcf_three_nums(nums):
    if len(nums) < 85:
        return None
    return math.gcd(math.gcd(nums[67], nums[84]), nums[13])