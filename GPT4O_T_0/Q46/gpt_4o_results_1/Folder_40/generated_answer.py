import math

def gcf_three_nums(nums):
    if len(nums) < 9:
        return None
    return math.gcd(math.gcd(nums[1], nums[6]), nums[8])