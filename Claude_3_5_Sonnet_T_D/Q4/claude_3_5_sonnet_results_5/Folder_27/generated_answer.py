def all_pos_ints_exclusive(int_list):
    if len(int_list) <= 29:
        return []
    return [num for num in int_list[29:49] if num > 0]