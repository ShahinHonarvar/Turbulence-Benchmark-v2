def sum_ints_div_by_either_nums(int_list):
    return sum((x for x in int_list[58:76] if x % 72 == 0 or x % 62 == 0))