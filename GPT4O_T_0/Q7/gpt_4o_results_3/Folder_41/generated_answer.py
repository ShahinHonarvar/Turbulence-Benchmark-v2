def all_even_ints_inclusive(lst):
    if len(lst) < 7:
        return []
    return [x for x in lst[6:7] if x % 2 == 0]