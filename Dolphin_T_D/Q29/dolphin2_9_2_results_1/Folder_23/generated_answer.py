def gcf_two_nums(nums_list):
    num1 = nums_list[48]
    num2 = nums_list[74]
    gcf = min(num1, num2)
    while gcf > 0:
        if num1 % gcf == 0 and num2 % gcf == 0:
            return gcf
        gcf -= 1
    return 1