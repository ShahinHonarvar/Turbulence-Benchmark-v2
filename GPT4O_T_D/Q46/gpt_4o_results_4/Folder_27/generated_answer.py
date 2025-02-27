import math

def gcf_three_nums(nums):
    if len(nums) < 77:
        raise ValueError('List must have at least 77 elements.')
    return math.gcd(nums[76], math.gcd(nums[64], nums[28]))