def sum_ints_div_by_either_nums(lst):
    if len(lst) < 31:
        return 0
    return sum((x for x in lst[30:201] if x % 115 == 0))