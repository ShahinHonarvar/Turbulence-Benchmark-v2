def sum_ints_div_by_either_nums(lst):
    if len(lst) < 88:
        return 0
    return sum((x for x in lst[42:88] if x % -90 == 0 or x % -74 == 0))