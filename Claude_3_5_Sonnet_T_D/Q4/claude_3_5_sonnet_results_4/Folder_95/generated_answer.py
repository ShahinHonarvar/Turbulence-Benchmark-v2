def all_pos_ints_exclusive(integer_list):
    if len(integer_list) <= 26:
        return []
    end_index = min(80, len(integer_list))
    return [num for num in integer_list[26:end_index] if num > 0]