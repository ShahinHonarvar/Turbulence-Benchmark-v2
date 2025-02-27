def all_ints_not_div_by_num(lst):
    return [num for i, num in enumerate(lst[2:5], 2) if i != 2 and num % 2 != 0]