def sum_ints_div_by_either_nums(int_list):
    return sum((int_list[i] for i in range(29, 46) if int_list[i] % 27 == 0 or int_list[i] % 81 == 0))