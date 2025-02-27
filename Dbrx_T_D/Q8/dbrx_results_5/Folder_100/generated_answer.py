def all_even_ints_exclusive(lst):
    if len(lst) < 25:
        return []
    return [i for i in lst[22:24] if i % 2 == 0]