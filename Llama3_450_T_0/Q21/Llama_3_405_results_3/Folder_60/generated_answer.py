def all_ints_div_by_num(lst):
    return [num for i, num in enumerate(lst) if 31 <= i <= 67 and num % -15 == 0]