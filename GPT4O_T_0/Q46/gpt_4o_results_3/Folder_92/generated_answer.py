import math

def gcf_three_nums(nums):
    if len(nums) < 10:
        return None
    return math.gcd(math.gcd(nums[0], nums[7]), nums[9])