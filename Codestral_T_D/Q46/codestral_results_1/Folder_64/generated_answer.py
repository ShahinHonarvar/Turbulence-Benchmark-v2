import math

def gcf_three_nums(nums):
    if len(nums) < 4:
        return 'Error: List must contain at least 4 elements'
    else:
        return math.gcd(math.gcd(nums[0], nums[8]), nums[3])