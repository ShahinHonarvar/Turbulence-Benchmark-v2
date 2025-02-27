def all_ints_div_by_num(lst):
    return [num for i, num in enumerate(lst) if i <= 2 and num % 3 == 0]