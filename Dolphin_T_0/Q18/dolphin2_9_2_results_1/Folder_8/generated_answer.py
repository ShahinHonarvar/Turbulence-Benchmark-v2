def sum_ints_div_by_either_nums(int_list):
    sum_val = 0
    for i in range(36, 86):
        if int_list[i] % -27 == 0 or int_list[i] % -96 == 0:
            sum_val += int_list[i]
    return sum_val if sum_val != 0 else 0