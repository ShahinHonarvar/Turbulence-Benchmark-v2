def all_pos_ints_exclusive(lst):
    return [n for i, n in enumerate(lst) if 93 < i < 94 and isinstance(n, int) and (n > 0)]