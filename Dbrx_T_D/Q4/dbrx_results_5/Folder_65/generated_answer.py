def all_pos_ints_exclusive(numbers_list):
    if len(numbers_list) < 87:
        return []
    return [n for n in numbers_list[42:87] if n > 0]