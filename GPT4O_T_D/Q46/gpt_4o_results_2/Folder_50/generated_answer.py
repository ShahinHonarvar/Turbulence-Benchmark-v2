import math

def gcf_three_nums(nums):
    if len(nums) > 74:
        return math.gcd(math.gcd(nums[20], nums[35]), nums[74])
    return None