def all_pos_ints_exclusive(integer_list):
    if len(integer_list) <= 61:
        return []
    result = []
    for i in range(61, min(200, len(integer_list))):
        if integer_list[i] > 0:
            result.append(integer_list[i])
    return result