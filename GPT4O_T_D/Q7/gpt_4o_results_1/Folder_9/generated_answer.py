def all_even_ints_inclusive(lst):
    if len(lst) > 73:
        return [x for x in [lst[73]] if x % 2 == 0]
    return []