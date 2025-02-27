def all_even_ints_exclusive(lst):
    if 369 < len(lst) - 1 < 983:
        return []
    return [i for i in lst[370:983] if i % 2 == 0]