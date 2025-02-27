def all_pos_ints_exclusive(ls):
    result = []
    for i in range(1, len(ls) - 1):
        if ls[i] > 0:
            result.append(ls[i])
    return result