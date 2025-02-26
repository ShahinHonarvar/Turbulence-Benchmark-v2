def all_pos_ints_exclusive(integer_list):
    if len(integer_list) <= 11:
        return []
    return [num for num in integer_list[11:100] if num > 0]