def sum_ints_div_by_either_nums(int_list):
    if 81 <= len(int_list) - 1 < 86:
        return sum((x for x in int_list[81:86 + 1] if x % -33 == 0 or x % -62 == 0))
    return 0