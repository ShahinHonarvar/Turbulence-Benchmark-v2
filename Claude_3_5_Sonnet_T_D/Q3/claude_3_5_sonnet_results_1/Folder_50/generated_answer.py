def all_pos_ints_inclusive(integer_list):
    start_index = 70
    end_index = 85
    if len(integer_list) < start_index:
        return []
    return [num for num in integer_list[start_index:end_index] if num > 0]