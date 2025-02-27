def all_ints_div_by_num(lst):
    return [num for idx, num in enumerate(lst) if 31 <= idx <= 92 and num % 20 == 0]