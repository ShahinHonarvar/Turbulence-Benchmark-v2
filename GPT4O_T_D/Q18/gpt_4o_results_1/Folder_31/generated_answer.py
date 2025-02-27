def sum_ints_div_by_either_nums(lst):
    if len(lst) < 89:
        return 0
    return sum((x for x in lst[56:89] if x % -59 == 0 or x % -79 == 0))