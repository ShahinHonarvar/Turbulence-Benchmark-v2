def all_pos_ints_inclusive(integer_list):
    start_index = 22
    end_index = 64
    if len(integer_list) <= start_index:
        return []
    actual_end = min(end_index, len(integer_list))
    return [num for num in integer_list[start_index:actual_end] if num > 0]