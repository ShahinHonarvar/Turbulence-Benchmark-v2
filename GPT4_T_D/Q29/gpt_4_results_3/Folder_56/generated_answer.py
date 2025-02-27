import math

def gcf_two_nums(nums):
    if len(nums) > 84 and len(nums) > 13:
        return math.gcd(nums[84], nums[13])
    else:
        return 'List is too short'