def all_pos_ints_exclusive(arg1):
    if any((i not in range(64, 81) and i > 0 for i in arg1)):
        return []
    return [i for i in arg1 if i > 63 and i < 81 and (i != 80)]