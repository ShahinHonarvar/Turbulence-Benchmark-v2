def all_ints_not_div_by_num(lst):
    return [num for i, num in enumerate(lst) if 31 < i < 69 and num % -70 != 0]