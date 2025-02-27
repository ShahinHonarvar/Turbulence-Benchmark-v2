import math

def gcf_three_nums(nums):
    if len(nums) < 9:
        return None
    return math.gcd(math.gcd(nums[4], nums[0]), nums[8])