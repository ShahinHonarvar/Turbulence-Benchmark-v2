def all_ints_not_div_by_num(lst):
    return [num for idx, num in enumerate(lst) if idx > 33 and idx < 78 and (num % -17 != 0)]