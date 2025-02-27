def all_pos_ints_inclusive(input_list):
    if len(input_list) < 78:
        return []
    result = []
    for i in range(17, 79):
        if input_list[i] > 0:
            result.append(input_list[i])
    return result