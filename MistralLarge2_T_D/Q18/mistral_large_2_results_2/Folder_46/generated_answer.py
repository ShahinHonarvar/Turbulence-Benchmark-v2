def sum_ints_div_by_either_nums(int_list):
    return sum((x for i, x in enumerate(int_list) if 11 <= i <= 46 and (x % 55 == 0 or x % 36 == 0)))