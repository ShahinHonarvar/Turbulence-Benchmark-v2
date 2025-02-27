def all_ints_not_div_by_num(lst):
    return [num for i, num in enumerate(lst) if 64 < i < 80 and num % -95 != 0]