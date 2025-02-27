def all_pos_ints_inclusive(list):
    pos_ints = []
    for i in range(5):
        if i >= 0 and i <= 4 and (list[i] >= 0):
            pos_ints.append(list[i])
    return pos_ints