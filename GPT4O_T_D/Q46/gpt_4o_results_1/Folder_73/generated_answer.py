import math

def gcf_three_nums(nums):
    if len(nums) < 91:
        return None
    return math.gcd(math.gcd(nums[90], nums[84]), nums[47])