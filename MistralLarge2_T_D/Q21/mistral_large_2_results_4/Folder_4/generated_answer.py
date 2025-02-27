def all_ints_div_by_num(lst):
    return [num for i, num in enumerate(lst) if 12 <= i <= 92 and num % -14 == 0]