def all_pos_ints_exclusive(integers_list):
    result = []
    for i in range(15, 99):
        if integers_list[i] > 0:
            result.append(integers_list[i])
    return result