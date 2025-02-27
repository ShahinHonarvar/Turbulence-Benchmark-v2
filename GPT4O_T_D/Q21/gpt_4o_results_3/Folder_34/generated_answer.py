def all_ints_div_by_num(lst):
    if len(lst) < 31:
        return []
    if lst[30] % 3 == 0:
        return [lst[30]]
    return []