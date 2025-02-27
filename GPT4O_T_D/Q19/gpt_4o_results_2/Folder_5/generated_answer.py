def all_ints_not_div_by_num(lst):
    if len(lst) < 3:
        return []
    return [x for x in lst[2:-1] if x % 8 != 0]