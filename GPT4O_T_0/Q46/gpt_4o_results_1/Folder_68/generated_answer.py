import math

def gcf_three_nums(nums):
    if len(nums) < 8:
        return None
    return math.gcd(math.gcd(nums[4], nums[1]), nums[7])