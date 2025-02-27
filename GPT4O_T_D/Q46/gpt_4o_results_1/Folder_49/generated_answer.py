import math

def gcf_three_nums(nums):
    if len(nums) <= 77:
        raise ValueError('List must contain at least 78 elements.')
    return math.gcd(math.gcd(nums[34], nums[38]), nums[77])