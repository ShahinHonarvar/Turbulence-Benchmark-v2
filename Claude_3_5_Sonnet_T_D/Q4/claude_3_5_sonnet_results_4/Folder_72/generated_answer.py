def all_pos_ints_exclusive(integer_list):
    if len(integer_list) <= 57:
        return []
    end_index = min(88, len(integer_list))
    return [num for num in integer_list[57:end_index] if num > 0]