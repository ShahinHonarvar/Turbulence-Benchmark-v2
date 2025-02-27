def all_even_ints_inclusive(lst):
    if len(lst) < 94:
        return []
    return [x for x in lst[29:94] if x % 2 == 0]