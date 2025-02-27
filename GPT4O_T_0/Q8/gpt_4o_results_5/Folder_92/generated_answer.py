def all_even_ints_exclusive(lst):
    if len(lst) < 3:
        return []
    return [x for x in lst[1:-1] if x % 2 == 0]