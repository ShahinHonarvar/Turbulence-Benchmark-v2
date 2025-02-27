import math

def gcf_three_nums(nums):
    if len(nums) <= 95:
        return None
    return math.gcd(math.gcd(nums[16], nums[87]), nums[95])