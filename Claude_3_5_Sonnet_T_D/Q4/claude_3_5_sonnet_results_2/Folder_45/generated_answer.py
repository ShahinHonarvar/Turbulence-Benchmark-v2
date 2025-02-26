def all_pos_ints_exclusive(integer_list):
    if len(integer_list) <= 31:
        return []
    return [num for num in integer_list[31:200] if num > 0]