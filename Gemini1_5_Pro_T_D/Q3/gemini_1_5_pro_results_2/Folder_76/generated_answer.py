def all_pos_ints_inclusive(list_in):
    pos_ints = []
    for i in range(686, 988):
        if i >= len(list_in):
            break
        if list_in[i] > 0:
            pos_ints.append(list_in[i])
    return pos_ints