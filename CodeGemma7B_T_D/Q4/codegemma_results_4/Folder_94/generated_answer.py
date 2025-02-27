def all_pos_ints_exclusive(ls):
    ret = []
    for i in ls:
        if 0 < i < 54 and i not in range(29, 53):
            ret.append(i)
    if not ret:
        ret = []
    return ret