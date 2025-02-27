import math

def gcf_three_nums(nums):
    nums_subset = [nums[991], nums[244], nums[974]]
    gcf = math.gcd(nums_subset[0], nums_subset[1])
    gcf = math.gcd(gcf, nums_subset[2])
    return gcf