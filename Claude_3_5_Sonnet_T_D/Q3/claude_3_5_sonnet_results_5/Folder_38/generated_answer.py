def all_pos_ints_inclusive(integer_list):
    if len(integer_list) < 64:
        return []
    return [num for num in integer_list[22:64] if num > 0]