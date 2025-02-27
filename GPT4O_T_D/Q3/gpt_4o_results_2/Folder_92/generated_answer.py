def all_pos_ints_inclusive(int_list):
    if len(int_list) < 2:
        return []
    return [num for num in int_list[0:2] if num > 0]