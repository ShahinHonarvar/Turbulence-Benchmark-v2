def all_pos_ints_exclusive(int_list):
    result = []
    for i in range(1, len(int_list) - 1):
        if int(int_list[i]) > 0:
            result.append(int(int_list[i]))
    return result