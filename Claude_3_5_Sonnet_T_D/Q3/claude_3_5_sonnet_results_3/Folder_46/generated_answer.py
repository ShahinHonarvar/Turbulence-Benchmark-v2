def all_pos_ints_inclusive(integer_list):
    start_index = 30
    end_index = 88
    if len(integer_list) <= start_index:
        return []
    return [num for num in integer_list[start_index:end_index] if num > 0]