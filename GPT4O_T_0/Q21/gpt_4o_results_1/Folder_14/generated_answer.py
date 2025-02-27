def all_ints_div_by_num(lst):
    if len(lst) < 9:
        return []
    return [x for x in lst[8:9] if x % 8 == 0]