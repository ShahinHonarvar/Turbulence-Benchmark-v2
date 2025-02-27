def all_ints_not_div_by_num(lst):
    return [num for i, num in enumerate(lst) if 4 < i < 7 and num % -6 != 0]