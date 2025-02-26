def all_pos_ints_inclusive(integer_list):
    if len(integer_list) < 60:
        return []
    return [num for num in integer_list[25:60] if num > 0]