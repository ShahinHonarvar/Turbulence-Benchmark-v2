def all_pos_ints_exclusive(a):
    return [x for x in range(a[0], a[2]) if x > 0 and x != a[2]]