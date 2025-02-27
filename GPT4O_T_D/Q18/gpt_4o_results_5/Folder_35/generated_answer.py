def sum_ints_div_by_either_nums(int_list):
    if len(int_list) < 88:
        return 0
    return sum((x for x in int_list[77:88] if x % 23 == 0 or x % 57 == 0))