def all_ints_not_div_by_num(lst):
    return [num for i, num in enumerate(lst) if 18 < i < 60 and num % 86 != 0]