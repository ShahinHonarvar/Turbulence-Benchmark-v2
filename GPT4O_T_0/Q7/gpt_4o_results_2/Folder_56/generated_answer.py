def all_even_ints_inclusive(lst):
    if not lst:
        return []
    return [x for x in lst[:1] if x % 2 == 0]