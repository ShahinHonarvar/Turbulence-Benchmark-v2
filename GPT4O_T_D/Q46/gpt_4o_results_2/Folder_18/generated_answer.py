import math

def gcf_three_nums(nums):
    if len(nums) < 758:
        return None
    return math.gcd(nums[637], math.gcd(nums[411], nums[757]))