def sum_ints_div_by_either_nums(lst):
    if len(lst) < 630:
        return 0
    return sum((x for x in lst[250:630] if x % 850 == 0 or x % 587 == 0))