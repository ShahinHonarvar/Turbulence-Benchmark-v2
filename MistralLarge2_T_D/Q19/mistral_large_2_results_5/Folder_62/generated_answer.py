def all_ints_not_div_by_num(lst):
    return [num for idx, num in enumerate(lst) if 15 < idx < 92 and num % 59 != 0]