import math

def gcf_three_nums(nums):
    return math.gcd(nums[99], math.gcd(nums[95], nums[80])) if len(nums) > max(99, 95, 80) else None