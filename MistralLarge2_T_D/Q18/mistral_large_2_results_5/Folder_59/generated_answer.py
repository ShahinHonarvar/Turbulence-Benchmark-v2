def sum_ints_div_by_either_nums(int_list):
    return sum((x for x in int_list[:9] if x % -3 == 0 or x % 8 == 0))