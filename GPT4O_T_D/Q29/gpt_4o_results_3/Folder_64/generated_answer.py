import math

def gcf_two_nums(nums):
    if len(nums) > 9:
        return math.gcd(nums[6], nums[9])
    else:
        raise ValueError('List must contain at least 10 integers.')