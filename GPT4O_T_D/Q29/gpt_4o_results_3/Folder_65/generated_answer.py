import math

def gcf_two_nums(nums):
    if len(nums) > 53:
        return math.gcd(nums[29], nums[53])
    return None