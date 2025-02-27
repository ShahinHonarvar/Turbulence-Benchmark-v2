def all_ints_not_div_by_num(lst):
    indices = range(32, 54)
    result = [x for i, x in enumerate(lst) if i in indices and x % -97 != 0]
    return result