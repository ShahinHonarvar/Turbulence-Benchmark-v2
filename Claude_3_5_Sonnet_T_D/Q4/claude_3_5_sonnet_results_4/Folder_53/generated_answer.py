def all_pos_ints_exclusive(integer_list):
    if len(integer_list) <= 201:
        return []
    return [num for num in integer_list[101:200] if num > 0]