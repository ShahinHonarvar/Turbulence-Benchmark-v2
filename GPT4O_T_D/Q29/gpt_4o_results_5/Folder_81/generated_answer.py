import math

def gcf_two_nums(nums):
    if len(nums) > 83:
        return math.gcd(nums[20], nums[83])
    return None