def all_pos_ints_exclusive(integer_list):
    if len(integer_list) <= 45:
        return []
    return [num for num in integer_list[24:45] if num > 0]