def all_ints_not_div_by_num(lst):
    return [num for i, num in enumerate(lst) if 48 < i < 92 and num % 90 != 0]