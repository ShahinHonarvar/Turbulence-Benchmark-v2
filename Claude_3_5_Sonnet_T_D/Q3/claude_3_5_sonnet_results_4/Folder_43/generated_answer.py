def all_pos_ints_inclusive(integer_list):
    if len(integer_list) < 87:
        return []
    return [num for num in integer_list[68:87] if num > 0]