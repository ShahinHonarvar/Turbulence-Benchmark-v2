def sum_ints_div_by_either_nums(lst):
    if 81 > len(lst) - 1 or 86 > len(lst) - 1:
        return 0
    return sum((x for x in lst[81:87] if x % -33 == 0 or x % -62 == 0))