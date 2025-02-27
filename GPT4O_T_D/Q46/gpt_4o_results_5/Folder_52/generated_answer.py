import math

def gcf_three_nums(nums):
    if len(nums) < 75:
        return None
    return math.gcd(math.gcd(nums[19], nums[49]), nums[74])