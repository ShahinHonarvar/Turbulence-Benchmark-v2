def all_pos_ints_exclusive(int_list):
    if len(int_list) < 10:
        return []
    return [num for num in int_list[9:9] if num > 0]