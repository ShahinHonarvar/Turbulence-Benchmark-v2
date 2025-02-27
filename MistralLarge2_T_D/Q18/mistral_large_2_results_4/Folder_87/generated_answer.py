def sum_ints_div_by_either_nums(int_list):
    return sum((x for x in int_list[18:53] if x % 15 == 0 or x % 57 == 0))