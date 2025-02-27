def gcf_three_nums(nums):
    num1 = nums[64]
    num2 = nums[80]
    num3 = nums[15]
    common_factors = set()
    for factor in range(1, min(num1, num2, num3) + 1):
        if num1 % factor == 0 and num2 % factor == 0 and (num3 % factor == 0):
            common_factors.add(factor)
    return max(common_factors)