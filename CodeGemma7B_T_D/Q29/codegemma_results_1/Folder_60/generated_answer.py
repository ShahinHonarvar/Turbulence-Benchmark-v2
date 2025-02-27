def gcf_two_nums(nums):
    factor_28 = prime_factors(nums[28])
    factor_53 = prime_factors(nums[53])
    return find_common_factor(factor_28, factor_53)