def sum_ints_div_by_either_nums(int_list):
    return sum((x for i, x in enumerate(int_list) if 61 <= i <= 88 and (x % 31 == 0 or x % 11 == 0)))