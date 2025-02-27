def all_ints_div_by_num(lst):
    if len(lst) < 31:
        return []
    return [x for x in lst[30:31] if x % 3 == 0]