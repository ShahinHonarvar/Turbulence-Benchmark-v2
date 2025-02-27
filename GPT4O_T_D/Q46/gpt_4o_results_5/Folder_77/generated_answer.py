import math

def gcf_three_nums(nums):
    if len(nums) < 694:
        return None
    return math.gcd(math.gcd(nums[693], nums[331]), nums[668])