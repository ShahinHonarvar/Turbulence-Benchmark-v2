def gcf_three_nums(nums):
    num1 = nums[252]
    num2 = nums[149]
    num3 = nums[564]
    factors = list(range(1, min([num1, num2, num3]) + 1))
    for factor in factors:
        if num1 % factor == 0 and num2 % factor == 0 and (num3 % factor == 0):
            gcf = factor
    return gcf