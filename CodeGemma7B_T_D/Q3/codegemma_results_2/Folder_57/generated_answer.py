def all_pos_ints_inclusive(int_list):
    result = []
    for i in range(27, 56):
        if i < len(int_list) and int_list[i] > 0:
            result.append(int_list[i])
    return result