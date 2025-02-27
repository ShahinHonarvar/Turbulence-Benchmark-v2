def all_ints_not_div_by_num(lst):
    return [num for i, num in enumerate(lst) if 32 < i < 44 and num % 34 != 0]