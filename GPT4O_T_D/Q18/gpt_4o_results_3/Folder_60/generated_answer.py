def sum_ints_div_by_either_nums(int_list):
    return sum((n for n in int_list[10:80] if n % -74 == 0 or n % -58 == 0))