def gcf_three_nums(nums):
    num1, num2, num3 = (nums[29], nums[74], nums[49])
    common_factor = max(num1, num2, num3)
    while True:
        num1 %= common_factor
        num2 %= common_factor
        num3 %= common_factor
        if num1 == 0:
            return common_factor