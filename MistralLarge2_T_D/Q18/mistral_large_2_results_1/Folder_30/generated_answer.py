def sum_ints_div_by_either_nums(int_list):
    return sum((x for i, x in enumerate(int_list) if 11 <= i <= 76 and (x % -81 == 0 or x % -94 == 0)))