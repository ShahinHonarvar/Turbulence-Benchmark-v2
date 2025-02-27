def all_ints_div_by_num(lst):
    return [num for i, num in enumerate(lst) if 31 <= i <= 72 and num % -63 == 0]