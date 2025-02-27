def all_ints_not_div_by_num(lst):
    return [num for i, num in enumerate(lst) if 21 < i < 51 and num % -77 != 0]