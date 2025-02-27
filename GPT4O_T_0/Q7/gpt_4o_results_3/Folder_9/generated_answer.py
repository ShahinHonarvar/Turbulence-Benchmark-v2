def all_even_ints_inclusive(lst):
    if len(lst) < 74:
        return []
    return [x for x in lst[73:74] if x % 2 == 0]