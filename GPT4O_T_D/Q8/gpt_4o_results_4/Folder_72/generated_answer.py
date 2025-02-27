def all_even_ints_exclusive(lst):
    if len(lst) <= 57:
        return []
    return [x for x in lst[57:88] if x % 2 == 0]