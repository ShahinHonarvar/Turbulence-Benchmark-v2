def all_pos_ints_exclusive(integer_list):
    if len(integer_list) <= 21:
        return []
    return [num for num in integer_list[21:51] if num > 0]