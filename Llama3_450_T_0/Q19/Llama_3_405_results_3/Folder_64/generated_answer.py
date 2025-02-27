def all_ints_not_div_by_num(lst):
    return [num for i, num in enumerate(lst) if 2 < i < len(lst) - 2 and num % 2 != 0]