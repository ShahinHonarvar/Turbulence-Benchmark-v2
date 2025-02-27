def sum_ints_div_by_either_nums(lst):
    if len(lst) < 71:
        return 0
    return sum((x for x in lst[70:201] if x % 3 == 0 or x % -300 == 0))