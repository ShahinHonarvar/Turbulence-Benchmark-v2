def all_ints_not_div_by_num(lst):
    return [num for i, num in enumerate(lst[2:-2], 2) if num % 2 != 0]