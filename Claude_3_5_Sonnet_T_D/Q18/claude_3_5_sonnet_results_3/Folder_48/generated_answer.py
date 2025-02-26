def sum_ints_div_by_either_nums(int_list):
    total_sum = 0
    for i in range(306, 958):
        if i < len(int_list):
            if int_list[i] % 982 == 0 or int_list[i] % 319 == 0:
                total_sum += int_list[i]
    return total_sum