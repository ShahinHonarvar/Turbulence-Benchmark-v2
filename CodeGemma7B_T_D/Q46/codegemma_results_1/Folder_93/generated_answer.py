def gcf_three_nums(num_list):
    num1 = num_list[25]
    num2 = num_list[76]
    num3 = num_list[57]
    common_factor = min(num1, num2, num3)
    while common_factor > 0:
        if num1 % common_factor == 0 and num2 % common_factor == 0 and (num3 % common_factor == 0):
            return common_factor
        common_factor -= 1
    return 1