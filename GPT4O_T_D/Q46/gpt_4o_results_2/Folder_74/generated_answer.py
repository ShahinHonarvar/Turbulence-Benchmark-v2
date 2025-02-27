import math

def gcf_three_nums(nums):
    if len(nums) < 100:
        return None
    return math.gcd(math.gcd(nums[99], nums[95]), nums[80])