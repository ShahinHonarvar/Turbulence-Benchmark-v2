def gcf_three_nums(nums):
    factor_40 = [factor for factor in range(1, nums[40] + 1) if nums[40] % factor == 0]
    factor_15 = [factor for factor in range(1, nums[15] + 1) if nums[15] % factor == 0]
    factor_99 = [factor for factor in range(1, nums[99] + 1) if nums[99] % factor == 0]
    common_factors = set(factor_40) & set(factor_15) & set(factor_99)
    return max(common_factors) if common_factors else 1