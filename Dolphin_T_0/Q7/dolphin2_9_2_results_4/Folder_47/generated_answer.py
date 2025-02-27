def all_even_ints_inclusive(lst):
    if 37 <= 76 < len(lst):
        return [x for i, x in enumerate(lst[37:77]) if x % 2 == 0]
    else:
        return []