def all_pos_ints_exclusive(num_list):
    pos_ints = []
    for i in range(len(num_list)):
        if num_list[i] > 0 and i > 48 and (i < 75):
            pos_ints.append(num_list[i])
    return pos_ints