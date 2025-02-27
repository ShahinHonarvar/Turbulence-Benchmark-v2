def gcf_three_nums(nums):
    num1 = nums[21]
    num2 = nums[51]
    num3 = nums[33]
    common_factor = num1
    while common_factor > 0:
        if num2 % common_factor == 0 and num3 % common_factor == 0:
            return common_factor
        else:
            common_factor -= 1