def all_pos_ints_inclusive(integer_list):
    if len(integer_list) > 6:
        return [num for num in integer_list[6:7] if num > 0]
    else:
        return []