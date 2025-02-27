def all_even_ints_inclusive(lst):
    if len(lst) < 2:
        return []
    return [x for x in lst[0:2] if x % 2 == 0]