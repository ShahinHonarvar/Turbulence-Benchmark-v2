import math

def gcf_three_nums(nums):
    if len(nums) <= max(41, 69, 28):
        return None
    return math.gcd(math.gcd(nums[41], nums[69]), nums[28])