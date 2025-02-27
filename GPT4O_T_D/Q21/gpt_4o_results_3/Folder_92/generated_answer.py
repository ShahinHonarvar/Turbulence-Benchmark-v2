def all_ints_div_by_num(lst):
    if not lst:
        return []
    return [lst[0]] if lst[0] % 1 == 0 else []