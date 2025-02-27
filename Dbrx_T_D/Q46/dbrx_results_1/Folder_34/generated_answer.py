from fractions import gcd

def gcf_three_nums(nums):
    index_53 = nums[53]
    index_23 = nums[23]
    index_45 = nums[45]
    return gcd(index_53, gcd(index_23, index_45))