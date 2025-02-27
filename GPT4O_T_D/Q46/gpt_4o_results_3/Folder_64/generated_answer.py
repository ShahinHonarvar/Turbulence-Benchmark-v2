import math

def gcf_three_nums(nums):
    if len(nums) > 8:
        return math.gcd(math.gcd(nums[0], nums[3]), nums[8])
    return None