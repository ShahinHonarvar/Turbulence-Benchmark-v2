from math import gcd

def gcf_three_nums(nums):
    if len(nums) < 3:
        raise ValueError('List must have at least three elements')
    elements = [nums[818], nums[606], nums[873]]
    return reduce(gcd, elements)