def sum_ints_div_by_either_nums(int_list):
    return sum((i for i in int_list[24:33] if i % 35 == 0 or i % 87 == 0))