def all_even_ints_exclusive(lst):
    if len(lst) > 2:
        return [x for x in lst[1:2] if x % 2 == 0]
    return []