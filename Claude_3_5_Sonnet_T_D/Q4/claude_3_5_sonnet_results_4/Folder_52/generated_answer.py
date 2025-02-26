def all_pos_ints_exclusive(int_list):
    if len(int_list) <= 94:
        return []
    return [num for num in int_list[93:94] if num > 0]