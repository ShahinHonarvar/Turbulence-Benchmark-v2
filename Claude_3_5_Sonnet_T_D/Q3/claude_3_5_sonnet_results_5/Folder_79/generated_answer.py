def all_pos_ints_inclusive(integer_list):
    if len(integer_list) < 5:
        return []
    return [num for num in integer_list[4:5] if num > 0]