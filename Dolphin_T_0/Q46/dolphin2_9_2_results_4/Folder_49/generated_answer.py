def gcf_three_nums(nums):
    num1 = nums[34]
    num2 = nums[38]
    num3 = nums[77]
    gcf = min(num1, num2, num3)
    while gcf > 1:
        if num1 % gcf == 0 and num2 % gcf == 0 and (num3 % gcf == 0):
            break
        gcf -= 1
    return gcf