def all_even_ints_inclusive(lst):
    if len(lst) < 49:
        return []
    return [x for x in lst[30:49] if x % 2 == 0]