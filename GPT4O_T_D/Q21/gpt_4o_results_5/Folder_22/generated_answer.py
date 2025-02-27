def all_ints_div_by_num(lst):
    if len(lst) < 11:
        return []
    if lst[10] % 1 == 0:
        return [lst[10]]
    return []