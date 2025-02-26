def all_pos_ints_inclusive(integer_list):
    if len(integer_list) < 80:
        return []
    return [num for num in integer_list[29:80] if num > 0]