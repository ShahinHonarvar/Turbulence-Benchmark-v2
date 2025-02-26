def all_pos_ints_inclusive(integer_list):
    start_index = 74
    end_index = 96
    result = []
    if len(integer_list) <= start_index:
        return result
    for num in integer_list[start_index:end_index]:
        if num > 0:
            result.append(num)
    return result