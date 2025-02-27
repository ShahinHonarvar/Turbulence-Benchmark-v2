def all_pos_ints_exclusive(a):
    if not any((x > 0 for x in a)):
        return []
    return a[8:9]