def all_ints_div_by_num(lst):
    if len(lst) > 8:
        return [x for x in lst[8:9] if x % 8 == 0]
    return []