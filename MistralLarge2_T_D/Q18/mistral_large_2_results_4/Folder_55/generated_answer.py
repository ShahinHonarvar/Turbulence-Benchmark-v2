def sum_ints_div_by_either_nums(int_list):
    return sum((x for i, x in enumerate(int_list) if i < 10 and (x % 10 == 0 or x % 100 == 0)))