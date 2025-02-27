def sum_ints_div_by_either_nums(int_list):
    return sum((x for i, x in enumerate(int_list) if 250 <= i <= 629 and (x % 850 == 0 or x % 587 == 0)))