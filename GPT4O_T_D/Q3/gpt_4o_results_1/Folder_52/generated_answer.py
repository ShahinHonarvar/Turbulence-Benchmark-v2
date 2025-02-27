def all_pos_ints_inclusive(int_list):
    if len(int_list) < 39:
        return []
    return [num for num in int_list[28:39] if num > 0]