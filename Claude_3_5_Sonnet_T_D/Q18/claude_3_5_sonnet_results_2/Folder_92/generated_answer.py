def sum_ints_div_by_either_nums(int_list):
    if not int_list:
        return 0
    return int_list[0] if int_list[0] % 1 == 0 else 0