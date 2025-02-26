def all_pos_ints_exclusive(integer_list):
    if len(integer_list) <= 71:
        return []
    end_index = min(200, len(integer_list))
    return [num for num in integer_list[71:end_index] if num > 0]