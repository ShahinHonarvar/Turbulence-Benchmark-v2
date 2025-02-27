def all_ints_div_by_num(lst):
    result = [x for i, x in enumerate(lst) if i in range(18, 94) and x % -85 == 0]
    return result