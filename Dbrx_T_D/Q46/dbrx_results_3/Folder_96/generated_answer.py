from math import gcd

def gcf_three_nums(nums):
    nums_to_consider = [nums[29], nums[74], nums[49]]
    gcf = nums_to_consider[0]
    for num in nums_to_consider:
        gcf = gcd(gcf, num)
    return gcf