import math

def gcf_three_nums(nums):
    if len(nums) > 21:
        return math.gcd(math.gcd(nums[14], nums[21]), nums[17])
    return None