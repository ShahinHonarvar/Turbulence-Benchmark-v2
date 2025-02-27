def all_pos_ints_exclusive(l):
    result = []
    for i in range(15, 40):
        if l[i] > 0:
            result.append(l[i])
    return result