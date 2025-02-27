def all_pos_ints_inclusive(int_list):
    if len(int_list) < 100:
        return []
    return [num for num in int_list[62:100] if num > 0]