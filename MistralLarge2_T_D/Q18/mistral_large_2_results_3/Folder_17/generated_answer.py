def sum_ints_div_by_either_nums(int_list):
    return sum((x for i, x in enumerate(int_list) if 81 <= i <= 89 and (x % 56 == 0 or x % 68 == 0)))