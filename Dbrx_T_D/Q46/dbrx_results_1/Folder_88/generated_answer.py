import math

def gcf_three_nums(nums):
    nums_to_consider = [nums[47], nums[10], nums[28]]
    gcf = math.gcd(nums_to_consider[0], nums_to_consider[1])
    gcf = math.gcd(gcf, nums_to_consider[2])
    return gcf