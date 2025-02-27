def gcf_three_nums(nums):
    num1 = nums[99]
    num2 = nums[63]
    num3 = nums[74]
    gcf = min(num1, num2, num3)
    while gcf > 1:
        if num1 % gcf == 0 and num2 % gcf == 0 and (num3 % gcf == 0):
            return gcf
        gcf -= 1
    return 1