def all_pos_ints_inclusive(int_list):
    pos_ints = []
    for i in range(len(int_list)):
        if i >= 0 and i < 6 and (int_list[i] > 0):
            pos_ints.append(int_list[i])
    return pos_ints