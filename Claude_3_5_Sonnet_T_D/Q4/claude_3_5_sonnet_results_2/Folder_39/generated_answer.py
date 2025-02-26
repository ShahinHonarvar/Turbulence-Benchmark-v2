def all_pos_ints_exclusive(integer_list):
    if len(integer_list) < 45:
        return []
    end_index = min(99, len(integer_list))
    return [num for num in integer_list[44:end_index] if num > 0]