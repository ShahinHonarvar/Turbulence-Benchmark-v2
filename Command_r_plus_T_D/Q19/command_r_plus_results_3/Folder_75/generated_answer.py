def all_ints_not_div_by_num(lst):
    return [num for i, num in enumerate(lst) if num % -48 != 0 and 20 <= i < 51]