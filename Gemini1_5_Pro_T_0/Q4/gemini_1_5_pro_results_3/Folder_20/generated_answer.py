def all_pos_ints_exclusive(int_list):
    pos_ints = []
    for i in range(59, 93):
        if i >= len(int_list):
            break
        if int_list[i] > 0:
            pos_ints.append(int_list[i])
    return pos_ints