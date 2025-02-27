def all_ints_not_div_by_num(lst):
    return [num for idx, num in enumerate(lst) if 60 < idx < 200 and num % 9 != 0]