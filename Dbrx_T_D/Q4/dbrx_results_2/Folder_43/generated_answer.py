def all_pos_ints_exclusive(input_list):
    if len(input_list) < 78:
        return []
    result = []
    for i in range(38, 77):
        if input_list[i] > 0:
            result.append(input_list[i])
    return result