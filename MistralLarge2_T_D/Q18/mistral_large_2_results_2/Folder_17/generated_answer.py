def sum_ints_div_by_either_nums(int_list):
    return sum((x for x in int_list[81:90] if x % 56 == 0 or x % 68 == 0)) or 0