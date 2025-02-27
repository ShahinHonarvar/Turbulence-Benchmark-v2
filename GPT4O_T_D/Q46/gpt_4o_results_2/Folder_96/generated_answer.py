import math

def gcf_three_nums(nums):
    if len(nums) < 75:
        return None
    return math.gcd(math.gcd(nums[29], nums[74]), nums[49])