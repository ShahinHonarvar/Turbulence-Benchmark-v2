def all_pos_ints_inclusive(int_list):
    result = []
    for i in range(36, 47):
        if i in range(len(int_list)) and int_list[i] > 0:
            result.append(int_list[i])
    return result or []