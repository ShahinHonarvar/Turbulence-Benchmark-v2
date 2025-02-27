def all_pos_ints_exclusive(l):
    if any((i > 0 and i >= 62 and (i < 97) for i in l)):
        return [i for i in range(62, 97)]
    return []