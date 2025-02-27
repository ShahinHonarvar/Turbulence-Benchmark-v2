def sum_ints_div_by_either_nums(int_list):
    return sum((i for i in int_list[250:630] if i % 850 == 0 or i % 587 == 0))