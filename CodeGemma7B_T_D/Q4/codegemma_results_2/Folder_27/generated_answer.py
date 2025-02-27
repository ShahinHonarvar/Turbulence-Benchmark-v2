def all_pos_ints_exclusive(l):
    for i in range(28, 49):
        if l[i] > 0:
            return [l[i] for i in range(28, 49) if l[i] > 0]
    return []