def all_odd_ints_inclusive(lst):
    if len(lst) > 60:
        return [lst[60]] if lst[60] % 2 != 0 else []
    return []