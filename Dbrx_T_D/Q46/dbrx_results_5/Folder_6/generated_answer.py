from math import gcd

def apply_gcd(nums):
    return gcd(nums[0], nums[1])

def gcf_three_nums(numbers):
    nums_subset = [numbers[92], numbers[93], numbers[56]]
    return apply_gcd(nums_subset)