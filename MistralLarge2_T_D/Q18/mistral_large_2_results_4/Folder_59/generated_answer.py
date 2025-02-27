def sum_ints_div_by_either_nums(int_list):
    return sum((x for i, x in enumerate(int_list) if i <= 8 and (x % -3 == 0 or x % 8 == 0)))