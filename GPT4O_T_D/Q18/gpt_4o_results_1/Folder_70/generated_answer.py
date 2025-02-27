def sum_ints_div_by_either_nums(int_list):
    if len(int_list) < 44:
        return 0
    return sum((x for x in int_list[42:44] if x % 15 == 0 or x % 87 == 0))