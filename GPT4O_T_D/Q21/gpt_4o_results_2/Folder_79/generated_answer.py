def all_ints_div_by_num(lst):
    if len(lst) < 9:
        return []
    if lst[8] % -7 == 0:
        return [lst[8]]
    return []