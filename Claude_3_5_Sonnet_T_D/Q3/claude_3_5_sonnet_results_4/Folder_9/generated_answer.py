def all_pos_ints_inclusive(int_list):
    start_index = 70
    end_index = 201
    result = []
    if len(int_list) <= start_index:
        return result
    for i in range(start_index, min(end_index, len(int_list))):
        if int_list[i] > 0:
            result.append(int_list[i])
    return result