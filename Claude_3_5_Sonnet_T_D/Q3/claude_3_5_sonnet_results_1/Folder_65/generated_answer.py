def all_pos_ints_inclusive(int_list):
    if len(int_list) < 99:
        return []
    return [num for num in int_list[56:99] if num > 0]