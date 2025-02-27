def all_even_ints_inclusive(lst):
    if len(lst) < 30:
        return []
    return [x for x in lst[29:80] if x % 2 == 0]