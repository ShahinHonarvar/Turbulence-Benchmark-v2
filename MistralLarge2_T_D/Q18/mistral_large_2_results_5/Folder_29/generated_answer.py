def sum_ints_div_by_either_nums(int_list):
    return sum((x for x in int_list[55:85] if x % -24 == 0 or x % -11 == 0))