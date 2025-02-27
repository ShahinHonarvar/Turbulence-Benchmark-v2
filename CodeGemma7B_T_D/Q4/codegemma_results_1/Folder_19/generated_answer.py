def all_pos_ints_exclusive(l):
    result = []
    for i in range(2, 5):
        if l[i] > 0:
            result.append(l[i])
    return result