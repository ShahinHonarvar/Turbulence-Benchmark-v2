def all_pos_ints_exclusive(int_list):
    if len(int_list) <= 8:
        return []
    return [num for num in int_list[8:9] if num > 0]