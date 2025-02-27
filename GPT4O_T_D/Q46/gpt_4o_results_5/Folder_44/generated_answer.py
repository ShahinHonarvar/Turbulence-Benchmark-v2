import math

def gcf_three_nums(nums):
    if len(nums) < 97:
        return None
    return math.gcd(math.gcd(nums[62], nums[96]), nums[26])