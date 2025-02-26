def all_pos_ints_inclusive(integers):
    if len(integers) < 64:
        return []
    return [num for num in integers[62:64] if num > 0]