def all_pos_ints_inclusive(num_list):
    result = []
    for i in range(43, 87):
        if num_list[i] > 0:
            result.append(num_list[i])
    if not result:
        return []
    else:
        return result