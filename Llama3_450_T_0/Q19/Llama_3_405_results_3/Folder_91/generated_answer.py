def all_ints_not_div_by_num(lst):
    return [num for i, num in enumerate(lst[:4]) if num % 8 != 0]