def all_pos_ints_inclusive(l):
    pos_ints = []
    for i in range(max(0, min(len(l) - 1, 74)), min(len(l), 96)):
        if l[i] > 0:
            pos_ints.append(l[i])
    return pos_ints