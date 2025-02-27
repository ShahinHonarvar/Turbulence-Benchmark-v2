import math

def gcf_three_nums(nums):
    if len(nums) < 99:
        return None
    return math.gcd(math.gcd(nums[70], nums[98]), nums[22])