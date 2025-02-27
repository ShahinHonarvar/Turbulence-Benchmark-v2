def sum_ints_div_by_either_nums(int_list):
    return sum((x for x in int_list[90:98] if x % 13 == 0 or x % 35 == 0))