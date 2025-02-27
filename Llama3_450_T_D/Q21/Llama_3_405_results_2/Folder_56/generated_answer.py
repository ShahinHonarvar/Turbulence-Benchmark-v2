def all_ints_div_by_num(lst):
    return [num for i, num in enumerate(lst) if 0 <= i <= 5 and num % 6 == 0]