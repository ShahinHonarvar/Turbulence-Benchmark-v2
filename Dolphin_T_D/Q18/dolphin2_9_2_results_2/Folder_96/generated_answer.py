def sum_ints_div_by_either_nums(int_list):
    return sum((n for n in int_list[49:201] if n % 34 == 0 or n % 64 == 0))