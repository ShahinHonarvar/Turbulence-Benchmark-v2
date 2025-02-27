def all_ints_not_div_by_num(lst):
    return [num for i, num in enumerate(lst) if 13 < i < 70 and num % -78 != 0]