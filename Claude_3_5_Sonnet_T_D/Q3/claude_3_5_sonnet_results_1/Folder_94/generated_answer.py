def all_pos_ints_inclusive(integer_list):
    if len(integer_list) < 41:
        return []
    return [num for num in integer_list[28:41] if num > 0]