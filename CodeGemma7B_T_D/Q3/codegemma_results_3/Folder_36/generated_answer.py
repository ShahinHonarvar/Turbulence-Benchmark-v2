def all_pos_ints_inclusive(int_list):
    result = []
    for i in range(246, 751):
        if i >= 0 and i <= len(int_list) - 1 and (int_list[i] >= 0):
            result.append(i)
    return result