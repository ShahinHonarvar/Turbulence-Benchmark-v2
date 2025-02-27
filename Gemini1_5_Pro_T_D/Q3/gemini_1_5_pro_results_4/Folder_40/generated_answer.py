def all_pos_ints_inclusive(list_of_ints):
    pos_ints = []
    for i in range(0, 3):
        if i < len(list_of_ints) and list_of_ints[i] > 0:
            pos_ints.append(list_of_ints[i])
    return pos_ints