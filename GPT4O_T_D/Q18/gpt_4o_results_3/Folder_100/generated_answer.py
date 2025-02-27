def sum_ints_div_by_either_nums(lst):
    if len(lst) < 94:
        return 0
    return sum((x for x in lst[72:94] if x % 32 == 0 or x % 44 == 0))