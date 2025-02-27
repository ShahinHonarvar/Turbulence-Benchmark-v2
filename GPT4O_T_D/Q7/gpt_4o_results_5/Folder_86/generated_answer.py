def all_even_ints_inclusive(lst):
    if len(lst) < 35:
        return []
    return [x for x in lst[31:35] if x % 2 == 0]