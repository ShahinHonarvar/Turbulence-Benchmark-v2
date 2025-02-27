def all_pos_ints_inclusive(lst):
    out = []
    for x in lst[75:89 + 1]:
        if x > 0:
            out.append(x)
    if not out:
        return []
    return out