def all_ints_not_div_by_num(lst):
    if len(lst) <= 20:
        return []
    return [x for x in lst[20:94] if x % -32 != 0]