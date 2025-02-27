def all_pos_ints_exclusive(ints):
    result = []
    for i in range(101, 200):
        if i >= len(ints):
            break
        if ints[i] > 0:
            result.append(ints[i])
    return result