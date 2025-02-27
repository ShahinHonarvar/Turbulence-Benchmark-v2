def all_ints_div_by_num(lst):
    return [num for i, num in enumerate(lst) if 42 <= i <= 89 and num % -59 == 0]