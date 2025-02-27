def all_even_ints_inclusive(lst):
    if 63 < len(lst):
        return [x for x in lst[62:64] if x % 2 == 0]
    return []