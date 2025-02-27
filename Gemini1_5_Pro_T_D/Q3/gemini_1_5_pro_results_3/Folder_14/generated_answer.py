def all_pos_ints_inclusive(list1):
    pos_ints = []
    for i in range(5, 8):
        if i in range(len(list1)):
            if list1[i] > 0:
                pos_ints.append(list1[i])
    return pos_ints