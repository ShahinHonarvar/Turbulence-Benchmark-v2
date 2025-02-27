import math

def gcf_three_nums(nums):
    a = nums[31]
    b = nums[69]
    c = nums[40]
    factors_a = [i for i in range(1, a + 1) if a % i == 0]
    factors_b = [j for j in range(1, b + 1) if b % j == 0]
    factors_c = [k for k in range(1, c + 1) if c % k == 0]
    common_factors = [factor for factor in factors_a if factor in factors_b and factor in factors_c]
    return max(common_factors)