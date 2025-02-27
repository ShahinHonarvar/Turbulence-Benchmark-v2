def all_ints_not_div_by_num(lst):
    result = [val for i, val in enumerate(lst) if i > 48 and i < 92 and (val % 90 != 0)]
    return result