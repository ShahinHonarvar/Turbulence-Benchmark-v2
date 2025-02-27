def all_ints_div_by_num(lst):
    return [num for i, num in enumerate(lst) if 20 <= i <= 200 and num % 4 == 0]