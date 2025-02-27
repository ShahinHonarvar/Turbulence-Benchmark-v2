def sum_ints_div_by_either_nums(int_list):
    return sum((x for i, x in enumerate(int_list) if 34 <= i <= 81 and (x % 27 == 0 or x % 57 == 0)))