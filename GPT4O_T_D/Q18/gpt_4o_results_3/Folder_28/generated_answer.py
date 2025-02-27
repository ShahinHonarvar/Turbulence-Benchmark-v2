def sum_ints_div_by_either_nums(lst):
    if len(lst) < 82:
        return 0
    return sum((n for n in lst[34:82] if n % 27 == 0 or n % 57 == 0))