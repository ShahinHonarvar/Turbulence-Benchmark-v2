def all_even_ints_inclusive(lst):
    if len(lst) < 52:
        return []
    return [x for x in lst[29:52] if x % 2 == 0]