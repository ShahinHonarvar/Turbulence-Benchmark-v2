import math

def gcf_two_nums(nums):
    if len(nums) > 53:
        return math.gcd(nums[49], nums[53])
    return None