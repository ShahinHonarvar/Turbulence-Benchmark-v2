def all_pos_ints_inclusive(integer_list):
    if len(integer_list) < 7:
        return []
    return [num for num in integer_list[6:7] if num > 0]