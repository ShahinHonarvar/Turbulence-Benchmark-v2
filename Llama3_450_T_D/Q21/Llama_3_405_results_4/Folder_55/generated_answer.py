def all_ints_div_by_num(lst):
    return [num for i, num in enumerate(lst) if i <= 1 and num % 2 == 0]