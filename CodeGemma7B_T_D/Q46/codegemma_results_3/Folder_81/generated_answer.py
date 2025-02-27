def gcf_three_nums(num_list):
    num1 = num_list[20]
    num2 = num_list[17]
    num3 = num_list[28]
    common_factor = 1
    while num1 % common_factor == 0 and num2 % common_factor == 0 and (num3 % common_factor == 0):
        common_factor += 1
    return common_factor - 1