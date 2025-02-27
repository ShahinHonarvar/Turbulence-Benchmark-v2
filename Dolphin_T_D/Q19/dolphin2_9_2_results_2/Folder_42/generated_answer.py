def all_ints_not_div_by_num(lst):
    result = [x for i, x in enumerate(lst[11:56]) if i % 90 != 0]
    return result