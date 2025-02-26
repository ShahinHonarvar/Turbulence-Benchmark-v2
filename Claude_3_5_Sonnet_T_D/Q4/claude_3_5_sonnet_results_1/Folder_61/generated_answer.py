def all_pos_ints_exclusive(int_list):
    if len(int_list) <= 2:
        return []
    return [num for num in int_list[1:7] if num > 0]