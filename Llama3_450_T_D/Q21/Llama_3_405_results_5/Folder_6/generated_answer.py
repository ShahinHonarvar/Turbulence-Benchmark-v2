def all_ints_div_by_num(lst):
    return [num for i, num in enumerate(lst) if 13 <= i <= 63 and num % 46 == 0]