import math

def gcf_three_nums(nums):
    if len(nums) < 85:
        return None
    return math.gcd(math.gcd(nums[46], nums[84]), nums[23])