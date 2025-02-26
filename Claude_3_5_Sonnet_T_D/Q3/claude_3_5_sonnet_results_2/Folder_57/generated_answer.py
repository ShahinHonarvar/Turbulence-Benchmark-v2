def all_pos_ints_inclusive(integer_list):
    if len(integer_list) < 56:
        return []
    return [num for num in integer_list[27:56] if num > 0]