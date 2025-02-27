def all_ints_div_by_num(lst):
    result = [x for i, x in enumerate(lst[35:47], 36) if x % 28 == 0]
    return result