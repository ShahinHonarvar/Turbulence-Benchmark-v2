def gcf_three_nums(nums_list):
    num1 = nums_list[41]
    num2 = nums_list[69]
    num3 = nums_list[28]
    gcf = min(num1, num2, num3)
    while gcf > 1:
        if num1 % gcf == 0 and num2 % gcf == 0 and (num3 % gcf == 0):
            return gcf
        gcf -= 1
    return 1