def sum_ints_div_by_either_nums(int_list):
    total_sum = 0
    for i in range(24, 33):
        if i in int_list and (int_list[i] % 35 == 0 or int_list[i] % 87 == 0):
            total_sum += int_list[i]
    return total_sum