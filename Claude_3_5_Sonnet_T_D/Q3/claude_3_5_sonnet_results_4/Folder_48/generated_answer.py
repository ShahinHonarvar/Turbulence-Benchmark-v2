def all_pos_ints_inclusive(integer_list):
    start_index = 533
    end_index = 605
    result = []
    if len(integer_list) <= start_index:
        return result
    for i in range(start_index, min(end_index + 1, len(integer_list))):
        if integer_list[i] > 0:
            result.append(integer_list[i])
    return result