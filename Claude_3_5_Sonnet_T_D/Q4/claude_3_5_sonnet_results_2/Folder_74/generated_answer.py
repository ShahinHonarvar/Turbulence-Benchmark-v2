def all_pos_ints_exclusive(int_list):
    if len(int_list) <= 14:
        return []
    return [num for num in int_list[14:70] if num > 0]