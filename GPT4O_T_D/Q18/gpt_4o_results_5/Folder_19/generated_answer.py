def sum_ints_div_by_either_nums(lst):
    if len(lst) < 5:
        return 0
    return sum((x for x in lst[1:5] if x % 4 == 0 or x % -6 == 0))