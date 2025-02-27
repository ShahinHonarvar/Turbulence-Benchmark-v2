def all_pos_ints_inclusive(int_list):
    if len(int_list) < 37:
        return []
    return [num for num in int_list[33:37] if num > 0]