def all_even_ints_inclusive(lst):
    if len(lst) < 52:
        return []
    return [x for x in lst[52:72] if x % 2 == 0]