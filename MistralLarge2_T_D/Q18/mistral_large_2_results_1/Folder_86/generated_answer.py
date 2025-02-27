def sum_ints_div_by_either_nums(int_list):
    return sum((x for i, x in enumerate(int_list) if 54 <= i <= 79 and (x % 54 == 0 or x % 28 == 0)))