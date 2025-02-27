def sum_ints_div_by_either_nums(int_list):
    return sum((x for i, x in enumerate(int_list) if i <= 2 and (x % -2 == 0 or x % 3 == 0)))