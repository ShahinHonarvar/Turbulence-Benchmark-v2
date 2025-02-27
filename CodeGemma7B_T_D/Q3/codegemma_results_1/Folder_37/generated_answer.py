def all_pos_ints_inclusive(int_list):
    pos_ints = []
    for i in range(1, 6):
        try:
            int_list.index(i)
            pos_ints.append(i)
        except ValueError:
            pass
    return pos_ints