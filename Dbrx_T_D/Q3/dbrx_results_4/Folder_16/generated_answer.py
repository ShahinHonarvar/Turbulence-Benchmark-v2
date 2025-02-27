def all_pos_ints_inclusive(int_list):
    start = 33
    end = 36
    pos_ints = []
    for i in range(start, end + 1):
        if i >= len(int_list):
            break
        if int_list[i] > 0:
            pos_ints.append(int_list[i])
    return pos_ints