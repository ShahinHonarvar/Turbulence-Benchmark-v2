def all_ints_div_by_num(lst):
    if len(lst) == 0:
        return []
    elif lst[0] % 3 == 0:
        return [lst[0]]
    else:
        return []