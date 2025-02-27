def all_ints_div_by_num(lst):
    if len(lst) > 10:
        return [x for x in lst[10:11] if x % 1 == 0]
    return []