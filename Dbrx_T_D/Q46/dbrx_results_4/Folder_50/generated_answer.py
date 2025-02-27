import math

def gcf_three_nums(nums):
    a = nums[20]
    b = nums[35]
    c = nums[74]
    factor_a = [i for i in range(1, a + 1) if a % i == 0]
    factor_b = [i for i in range(1, b + 1) if b % i == 0]
    factor_c = [i for i in range(1, c + 1) if c % i == 0]
    common_factors = [val for val in factor_a if val in factor_b and val in factor_c]
    return max(common_factors)