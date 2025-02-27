def sum_ints_div_by_either_nums(int_list):
    return sum((x for x in int_list[0:4] if x % 11 == 0 or x % -7 == 0))