def all_pos_ints_inclusive(integer_list):
    start_index = 66
    end_index = 94
    if len(integer_list) <= start_index:
        return []
    return [num for num in integer_list[start_index:end_index] if num > 0]