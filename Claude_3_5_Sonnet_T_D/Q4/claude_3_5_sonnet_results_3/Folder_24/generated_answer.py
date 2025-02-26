def all_pos_ints_exclusive(int_list):
    if len(int_list) <= 14:
        return []
    end_index = min(66, len(int_list))
    return [num for num in int_list[14:end_index] if num > 0]