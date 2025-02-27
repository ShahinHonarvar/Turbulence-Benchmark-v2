def all_pos_ints_inclusive(int_list):
    pos_ints = []
    for i in range(min(len(int_list), 30), min(len(int_list), 20) - 1, -1):
        if int_list[i] > 0:
            pos_ints.append(int_list[i])
    return pos_ints[::-1] if pos_ints else []