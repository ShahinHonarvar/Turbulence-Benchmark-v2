import math

def gcf_three_nums(nums):
    if len(nums) <= 92:
        return None
    return math.gcd(math.gcd(nums[66], nums[56]), nums[92])