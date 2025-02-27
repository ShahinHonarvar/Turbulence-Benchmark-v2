def all_pos_ints_inclusive(int_list):
    pos_ints = []
    for i in range(25, 88):
        if i > 0 and i in int_list:
            pos_ints.append(i)
    return pos_ints