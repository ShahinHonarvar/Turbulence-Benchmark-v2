import math

def gcf_two_nums(nums):
    if len(nums) > 54:
        return math.gcd(nums[36], nums[54])
    else:
        return None