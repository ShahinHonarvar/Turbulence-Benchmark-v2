def all_pos_ints_exclusive(int_list):
    if len(int_list) <= 386:
        return []
    return [num for num in int_list[386:999] if num > 0]