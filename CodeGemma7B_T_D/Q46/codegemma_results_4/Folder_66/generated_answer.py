from math import gcd

def gcf_three_nums(nums):
    num_92 = nums[92]
    num_69 = nums[69]
    num_95 = nums[95]
    common_factor = gcd(num_92, gcd(num_69, num_95))
    return common_factor