def sum_ints_div_by_either_nums(lst):
    if 22 > len(lst) - 1 or 24 > len(lst) - 1:
        return 0
    return sum((x for x in lst[22:25] if x % -85 == 0 or x % -30 == 0))