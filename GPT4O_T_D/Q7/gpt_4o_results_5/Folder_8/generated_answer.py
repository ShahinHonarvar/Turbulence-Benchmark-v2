def all_even_ints_inclusive(lst):
    if len(lst) < 24:
        return []
    if lst[23] % 2 == 0:
        return [lst[23]]
    return []