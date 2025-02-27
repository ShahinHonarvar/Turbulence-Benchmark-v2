def sum_ints_div_by_either_nums(int_list):
    if len(int_list) < 85:
        return 0
    return sum((x for x in int_list[57:85] if x % -30 == 0 or x % -88 == 0))