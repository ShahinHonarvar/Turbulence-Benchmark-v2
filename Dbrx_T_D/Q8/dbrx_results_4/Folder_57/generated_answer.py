def all_even_ints_exclusive(lst):
    if len(lst) < 38:
        return []
    return [i for i in lst[18:37] if i % 2 == 0]