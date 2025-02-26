def all_pos_ints_exclusive(integer_list):
    if len(integer_list) <= 2:
        return []
    return [num for num in integer_list[1:9] if num > 0]