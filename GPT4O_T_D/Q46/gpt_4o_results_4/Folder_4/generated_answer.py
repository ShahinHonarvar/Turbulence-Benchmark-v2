import math

def gcf_three_nums(nums):
    if len(nums) <= 80:
        return None
    return math.gcd(math.gcd(nums[24], nums[25]), nums[80])