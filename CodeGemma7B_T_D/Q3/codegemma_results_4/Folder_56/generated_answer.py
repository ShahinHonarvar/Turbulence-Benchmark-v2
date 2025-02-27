def all_pos_ints_inclusive(int_list):
    i = 1
    pos_int_list = []
    while i <= len(int_list):
        if int_list[i - 1] >= 0:
            pos_int_list.append(int_list[i - 1])
        i += 1
    return pos_int_list