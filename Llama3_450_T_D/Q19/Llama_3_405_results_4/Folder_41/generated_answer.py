def all_ints_not_div_by_num(lst):
    return [num for i, num in enumerate(lst) if 0 < i < 8 and num % -3 != 0]