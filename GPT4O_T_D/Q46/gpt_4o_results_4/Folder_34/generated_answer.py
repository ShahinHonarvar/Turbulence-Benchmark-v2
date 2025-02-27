import math

def gcf_three_nums(nums):
    if len(nums) < 54:
        return None
    a = nums[53]
    b = nums[23]
    c = nums[45]
    return math.gcd(math.gcd(a, b), c)