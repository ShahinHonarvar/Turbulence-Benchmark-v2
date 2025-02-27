def all_pos_ints_exclusive(int_list):
    result = []
    for i in range(36, 54):
        if int_list[i] > 0:
            result.append(int_list[i])
    return result