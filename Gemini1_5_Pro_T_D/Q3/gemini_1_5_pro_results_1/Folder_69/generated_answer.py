def all_pos_ints_inclusive(list1):
    pos_ints = []
    for i in range(32, 36):
        if i < len(list1) and list1[i] > 0:
            pos_ints.append(list1[i])
    return pos_ints