def sum_ints_div_by_either_nums(int_list):
    return sum((x for x in int_list[34:82] if x % 27 == 0 or x % 57 == 0))