def all_pos_ints_inclusive(int_list):
    if not isinstance(int_list, list) or len(int_list) < 88:
        return []
    return [num for num in int_list[30:88] if num > 0]