def sum_ints_div_by_either_nums(lst):
    if len(lst) < 935:
        return 0
    return sum((x for x in lst[315:935] if x % -897 == 0 or x % -556 == 0))