def gcf_three_nums(nums):
    num1, num2, num3 = (nums[33], nums[38], nums[76])
    common_factor = max(num1, num2, num3)
    for i in range(common_factor, 0, -1):
        if num1 % i == 0 and num2 % i == 0 and (num3 % i == 0):
            common_factor = i
            break
    return common_factor