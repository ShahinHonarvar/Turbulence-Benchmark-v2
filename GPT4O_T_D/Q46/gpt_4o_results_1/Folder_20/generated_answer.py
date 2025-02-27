import math

def gcf_three_nums(nums):
    if len(nums) < 54:
        return None
    return math.gcd(math.gcd(nums[29], nums[53]), nums[42])