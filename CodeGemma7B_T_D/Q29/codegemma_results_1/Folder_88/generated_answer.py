def gcf_two_nums(nums):
    num1 = nums[27]
    num2 = nums[34]
    common_factor = None
    for factor in range(min(num1, num2), 0, -1):
        if num1 % factor == 0 and num2 % factor == 0:
            common_factor = factor
            break
    return common_factor