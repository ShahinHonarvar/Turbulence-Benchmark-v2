def all_pos_ints_exclusive(int_list):
    pos_ints = []
    for i in range(8, len(int_list)):
        if int_list[i] > 0:
            pos_ints.append(int_list[i])
        if len(pos_ints) == 2:
            break
    return pos_ints