def all_pos_ints_inclusive(int_list):
    result = []
    for i in range(min(3, len(int_list))):
        if int_list[i] > 0:
            result.append(int_list[i])
    return result