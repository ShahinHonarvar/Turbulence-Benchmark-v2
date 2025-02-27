def all_pos_ints_inclusive(list_ints):
    pos_ints = []
    for i in range(64, 67):
        if list_ints[i] > 0:
            pos_ints.append(list_ints[i])
    return pos_ints