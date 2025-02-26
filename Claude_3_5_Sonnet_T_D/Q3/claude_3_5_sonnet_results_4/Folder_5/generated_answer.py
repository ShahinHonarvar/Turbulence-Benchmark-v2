def all_pos_ints_inclusive(integer_list):
    if len(integer_list) < 10:
        return []
    return [num for num in integer_list[8:10] if num > 0]