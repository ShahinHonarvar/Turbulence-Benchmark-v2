import math

def gcf_two_nums(nums):
    if len(nums) < 95:
        return None
    return math.gcd(nums[19], nums[94])