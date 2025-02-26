def all_pos_ints_inclusive(integer_list):
    if len(integer_list) < 49:
        return []
    return [num for num in integer_list[30:49] if num > 0]