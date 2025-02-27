import math

def gcf_three_nums(nums):
    if len(nums) < 975:
        return None
    return math.gcd(math.gcd(nums[991], nums[244]), nums[974])