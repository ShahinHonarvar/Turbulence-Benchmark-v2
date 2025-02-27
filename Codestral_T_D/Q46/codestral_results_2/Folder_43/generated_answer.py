import math

def gcf_three_nums(nums):
    if len(nums) > 93:
        return math.gcd(math.gcd(nums[33], nums[78]), nums[93])
    else:
        return 'The list does not contain the required indices.'