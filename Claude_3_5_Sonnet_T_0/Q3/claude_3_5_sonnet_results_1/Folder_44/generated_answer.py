def all_pos_ints_inclusive(integer_list):
    start_index = 13
    end_index = 69
    result = []
    if len(integer_list) <= start_index:
        return result
    for i in range(start_index, min(end_index, len(integer_list))):
        if integer_list[i] > 0:
            result.append(integer_list[i])
    return result