def sum_ints_div_by_either_nums(int_list):
    return sum((x for x in int_list[40:201] if x % 21 == 0 or x % 71 == 0))