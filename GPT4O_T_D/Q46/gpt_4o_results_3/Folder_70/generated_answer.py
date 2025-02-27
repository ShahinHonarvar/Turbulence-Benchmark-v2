import math

def gcf_three_nums(nums):
    if len(nums) < 712:
        return None
    return math.gcd(math.gcd(nums[990], nums[671]), nums[711])