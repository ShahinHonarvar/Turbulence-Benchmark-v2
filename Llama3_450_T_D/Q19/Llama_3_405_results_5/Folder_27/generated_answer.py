def all_ints_not_div_by_num(lst):
    return [num for i, num in enumerate(lst) if 14 < i < 21 and num % -93 != 0]