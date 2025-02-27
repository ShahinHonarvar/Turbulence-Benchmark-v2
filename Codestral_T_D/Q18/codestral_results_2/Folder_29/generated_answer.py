def sum_ints_div_by_either_nums(int_list):
    return sum((n for n in int_list[55:85] if n % -24 == 0 or n % -11 == 0))