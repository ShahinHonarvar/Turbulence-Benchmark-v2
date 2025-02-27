def sum_ints_div_by_either_nums(lst):
    if 81 >= len(lst) or 86 >= len(lst):
        return 0
    return sum((x for x in lst[81:87] if x % -33 == 0 or x % -62 == 0))