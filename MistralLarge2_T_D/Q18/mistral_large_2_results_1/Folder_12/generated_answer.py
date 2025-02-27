def sum_ints_div_by_either_nums(int_list):
    return sum((x for x in int_list[35:65] if x % -30 == 0 or x % -95 == 0))