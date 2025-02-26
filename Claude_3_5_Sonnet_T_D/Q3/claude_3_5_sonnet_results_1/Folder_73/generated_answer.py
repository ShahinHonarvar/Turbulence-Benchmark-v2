def all_pos_ints_inclusive(integer_list):
    if len(integer_list) < 93:
        return []
    return [num for num in integer_list[19:93] if num > 0]