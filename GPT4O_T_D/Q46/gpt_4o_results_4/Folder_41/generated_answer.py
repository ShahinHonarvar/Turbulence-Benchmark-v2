import math

def gcf_three_nums(nums):
    if len(nums) < 95:
        return None
    return math.gcd(math.gcd(nums[19], nums[94]), nums[78])