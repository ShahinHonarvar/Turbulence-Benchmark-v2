def all_pos_ints_inclusive(integers):
    if not integers or integers[0] <= 0:
        return []
    return [integers[0]]