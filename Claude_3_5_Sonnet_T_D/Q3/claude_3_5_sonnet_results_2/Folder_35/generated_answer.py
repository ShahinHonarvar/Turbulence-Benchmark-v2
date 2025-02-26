def all_pos_ints_inclusive(int_list):
    if len(int_list) < 49:
        return []
    return [num for num in int_list[30:49] if num > 0]