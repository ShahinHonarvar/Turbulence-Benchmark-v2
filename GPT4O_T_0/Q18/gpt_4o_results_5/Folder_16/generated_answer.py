def sum_ints_div_by_either_nums(lst):
    if len(lst) < 81:
        return 0
    return sum((x for x in lst[55:81] if x % 22 == 0 or x % 32 == 0))