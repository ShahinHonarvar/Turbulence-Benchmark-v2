def sum_ints_div_by_either_nums(lst):
    if len(lst) < 47:
        return 0
    return sum((x for x in lst[11:47] if x % 55 == 0 or x % 36 == 0))