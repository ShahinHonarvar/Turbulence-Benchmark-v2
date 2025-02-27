import math

def gcf_three_nums(nums):
    if len(nums) <= max(18, 10, 76):
        return None
    return math.gcd(math.gcd(nums[18], nums[10]), nums[76])