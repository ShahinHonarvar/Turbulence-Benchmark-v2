def all_pos_ints_inclusive(integer_list):
    if len(integer_list) < 88:
        return []
    return [num for num in integer_list[25:88] if num > 0]