import math

def gcf_three_nums(nums):
    a = nums[32]
    b = nums[54]
    c = nums[13]
    factors_a = [i for i in range(1, a + 1) if a % i == 0]
    factors_b = [i for i in range(1, b + 1) if b % i == 0]
    factors_c = [i for i in range(1, c + 1) if c % i == 0]
    common_factors = [val for val in factors_a if val in factors_b and val in factors_c]
    return max(common_factors)