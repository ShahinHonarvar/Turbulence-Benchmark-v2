def all_pos_ints_exclusive(integer_list):
    if len(integer_list) <= 63:
        return []
    start_index = 63
    end_index = min(96, len(integer_list))
    return [num for num in integer_list[start_index:end_index] if num > 0]