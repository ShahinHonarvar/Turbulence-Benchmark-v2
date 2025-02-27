import math

def gcf_three_nums(nums):
    if len(nums) > max(99, 28, 53):
        return math.gcd(math.gcd(nums[99], nums[28]), nums[53])
    return None