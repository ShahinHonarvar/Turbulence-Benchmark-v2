def all_even_ints_inclusive(lst):
    if len(lst) > 6:
        sublist = lst[6:7]
        return [x for x in sublist if x % 2 == 0]
    return []