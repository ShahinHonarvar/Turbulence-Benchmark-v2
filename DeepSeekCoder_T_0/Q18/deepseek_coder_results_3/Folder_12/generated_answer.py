def sum_ints_div_by_either_nums(lst):
    if len(lst) < 65:
        return 0
    return sum((x for x in lst[35:65] if x % -30 == 0 or x % -95 == 0))