def sum_ints_div_by_either_nums(int_list):
    return sum((x for x in int_list[306:958] if x % 982 == 0 or x % 319 == 0))