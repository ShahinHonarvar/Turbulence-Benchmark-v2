def all_pos_ints_inclusive(integer_list):
    if len(integer_list) < 100:
        return []
    return [num for num in integer_list[62:100] if num > 0]