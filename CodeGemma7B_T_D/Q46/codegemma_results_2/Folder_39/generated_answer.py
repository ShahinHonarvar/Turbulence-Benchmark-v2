def gcf_three_nums(nums):
    num1 = nums[85]
    num2 = nums[36]
    num3 = nums[54]
    common_factor = min((num1, num2, num3))
    while common_factor > 0:
        if num1 % common_factor == 0 and num2 % common_factor == 0 and (num3 % common_factor == 0):
            return common_factor
        else:
            common_factor -= 1