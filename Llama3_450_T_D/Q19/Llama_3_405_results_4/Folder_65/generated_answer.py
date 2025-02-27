def all_ints_not_div_by_num(lst):
    return [num for i, num in enumerate(lst) if 15 < i < 51 and num % -34 != 0]