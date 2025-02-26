def all_pos_ints_exclusive(integer_list):
    if len(integer_list) < 98:
        return []
    return [num for num in integer_list[70:97] if num > 0]