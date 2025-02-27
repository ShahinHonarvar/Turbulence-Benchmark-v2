def sum_ints_div_by_either_nums(int_list):
    return sum((x for i, x in enumerate(int_list) if 10 <= i <= 79 and (x % -74 == 0 or x % -58 == 0)))