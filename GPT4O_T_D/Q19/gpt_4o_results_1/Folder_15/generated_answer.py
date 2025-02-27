def all_ints_not_div_by_num(lst):
    if len(lst) <= 2:
        return []
    return [x for x in lst[1:2] if x % -2 != 0]