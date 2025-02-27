import math

def gcf_three_nums(nums):
    if len(nums) > 96:
        return math.gcd(math.gcd(nums[90], nums[54]), nums[96])
    return None