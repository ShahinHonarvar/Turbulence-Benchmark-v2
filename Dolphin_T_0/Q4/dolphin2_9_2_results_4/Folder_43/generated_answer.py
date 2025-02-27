def all_pos_ints_exclusive(ints):
    result = []
    for i in range(38, 78):
        if ints[i] > 0:
            result.append(ints[i])
    return result