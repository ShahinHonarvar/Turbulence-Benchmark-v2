def all_pos_ints_exclusive(list):
    pos_ints = []
    for i in range(38, 52):
        if list[i] > 0:
            pos_ints.append(list[i])
    return pos_ints