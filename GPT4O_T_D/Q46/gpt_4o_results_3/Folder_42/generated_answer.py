import math

def gcf_three_nums(nums):
    if len(nums) <= max(19, 69, 97):
        return None
    return math.gcd(math.gcd(nums[19], nums[69]), nums[97])