def all_even_ints_inclusive(lst):
    if not lst:
        return []
    elif lst[0] % 2 == 0:
        return [lst[0]]
    else:
        return []