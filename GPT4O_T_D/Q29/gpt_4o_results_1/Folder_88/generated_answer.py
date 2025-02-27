import math

def gcf_two_nums(nums):
    if len(nums) < 35:
        return None
    return math.gcd(nums[27], nums[34])