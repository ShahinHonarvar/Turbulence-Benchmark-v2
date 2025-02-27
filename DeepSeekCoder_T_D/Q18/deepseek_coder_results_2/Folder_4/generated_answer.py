def sum_ints_div_by_either_nums(lst):
    if 86 > 90 or 86 >= len(lst) or 90 >= len(lst):
        return 0
    return sum((x for x in lst[86:91] if x % -71 == 0 or x % -67 == 0))