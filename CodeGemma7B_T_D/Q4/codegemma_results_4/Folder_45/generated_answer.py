def all_pos_ints_exclusive(lst):
    out = []
    for i in range(30, 200):
        if lst[i] > 0:
            out.append(lst[i])
    if len(out) == 0:
        return []
    return out