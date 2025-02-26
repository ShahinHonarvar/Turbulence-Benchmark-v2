def all_pos_ints_inclusive(integer_list):
    if len(integer_list) < 99:
        return []
    return [num for num in integer_list[55:99] if num > 0]