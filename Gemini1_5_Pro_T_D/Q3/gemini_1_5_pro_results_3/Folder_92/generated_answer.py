def all_pos_ints_inclusive(int_list):
    result = []
    for i in range(len(int_list)):
        if i >= 0 and i <= 1 and (int_list[i] > 0):
            result.append(int_list[i])
    return result