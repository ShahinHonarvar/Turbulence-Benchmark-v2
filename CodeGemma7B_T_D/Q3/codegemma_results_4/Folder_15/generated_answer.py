def all_pos_ints_inclusive(int_list):
    pos_int_list = []
    if not int_list:
        return []
    for i in range(4):
        if i < len(int_list) and int_list[i] > 0:
            pos_int_list.append(int_list[i])
    return pos_int_list