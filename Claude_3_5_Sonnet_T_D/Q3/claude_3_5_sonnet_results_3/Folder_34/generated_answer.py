def all_pos_ints_inclusive(integer_list):
    if len(integer_list) < 61:
        return []
    end_index = min(201, len(integer_list))
    return [num for num in integer_list[60:end_index] if num > 0]