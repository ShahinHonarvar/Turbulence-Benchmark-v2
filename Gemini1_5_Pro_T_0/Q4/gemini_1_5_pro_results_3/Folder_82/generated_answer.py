def all_pos_ints_exclusive(int_list):
    result = []
    for i in range(21, 200):
        if i >= len(int_list):
            break
        if int_list[i] > 0:
            result.append(int_list[i])
    return result