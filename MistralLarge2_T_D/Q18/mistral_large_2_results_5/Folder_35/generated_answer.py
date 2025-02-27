def sum_ints_div_by_either_nums(int_list):
    return sum((x for x in int_list[77:88] if x % 23 == 0 or x % 57 == 0))