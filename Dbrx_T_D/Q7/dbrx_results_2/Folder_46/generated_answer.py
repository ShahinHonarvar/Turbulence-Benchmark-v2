def all_even_ints_inclusive(lst):
    if len(lst) < 88:
        return []
    return [i for i in lst[30:88] if i % 2 == 0]