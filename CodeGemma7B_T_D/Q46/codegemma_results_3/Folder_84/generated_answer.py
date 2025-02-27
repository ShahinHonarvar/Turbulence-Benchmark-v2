def gcf_three_nums(nums):
    num1, num2, num3 = (nums[695], nums[710], nums[914])
    common_factors = []
    for i in range(1, min(num1, num2, num3) + 1):
        if num1 % i == 0 and num2 % i == 0 and (num3 % i == 0):
            common_factors.append(i)
    return max(common_factors)