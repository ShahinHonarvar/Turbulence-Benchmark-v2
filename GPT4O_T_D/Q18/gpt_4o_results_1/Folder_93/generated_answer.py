def sum_ints_div_by_either_nums(int_list):
    if len(int_list) < 90:
        return 0
    return sum((x for x in int_list[86:90] if x % -61 == 0 or x % -79 == 0))