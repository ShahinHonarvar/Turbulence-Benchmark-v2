def all_ints_div_by_num(lst):
    if len(lst) > 0:
        if lst[0] % 2 == 0:
            return [lst[0]]
    return []