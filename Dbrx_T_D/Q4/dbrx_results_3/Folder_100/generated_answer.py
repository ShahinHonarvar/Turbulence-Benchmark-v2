def all_pos_ints_exclusive(int_list):
    result = []
    for i in range(len(int_list)):
        if i >= 22 and i < 24 and (int_list[i] > 0):
            result.append(int_list[i])
    return result