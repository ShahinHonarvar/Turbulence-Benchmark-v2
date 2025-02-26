def all_pos_ints_inclusive(integer_list):
    start_index = 37
    end_index = 77
    if len(integer_list) <= start_index:
        return []
    result = [num for num in integer_list[start_index:end_index] if num > 0]
    return result