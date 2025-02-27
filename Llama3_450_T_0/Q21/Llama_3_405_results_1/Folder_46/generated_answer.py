def all_ints_div_by_num(lst):
    return [num for i, num in enumerate(lst) if 21 <= i <= 97 and num % 46 == 0]