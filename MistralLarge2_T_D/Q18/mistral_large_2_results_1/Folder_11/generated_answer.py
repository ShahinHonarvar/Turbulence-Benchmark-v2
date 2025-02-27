def sum_ints_div_by_either_nums(int_list):
    return sum((x for i, x in enumerate(int_list) if 22 <= i <= 24 and (x % -85 == 0 or x % -30 == 0)))