def all_even_ints_inclusive(lst):
    if len(lst) < 65:
        return []
    else:
        return [i for i in lst[14:65] if i % 2 == 0]