import math

def gcf_three_nums(nums):
    if len(nums) < 70:
        raise ValueError('List must contain at least 70 elements')
    a, b, c = (nums[31], nums[69], nums[40])
    return math.gcd(math.gcd(a, b), c)