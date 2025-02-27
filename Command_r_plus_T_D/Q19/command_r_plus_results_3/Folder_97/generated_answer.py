def all_ints_not_div_by_num(lst):
    return [num for i, num in enumerate(lst[14:48], 14) if num % 16 != 0]