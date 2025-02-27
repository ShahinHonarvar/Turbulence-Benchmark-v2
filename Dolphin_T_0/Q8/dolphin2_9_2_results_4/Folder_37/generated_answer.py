def all_even_ints_exclusive(lst):
    result = [x for i, x in enumerate(lst) if 1 < i < 2 and x % 2 == 0]
    if result:
        return result
    return []