def all_pos_ints_inclusive(integers):
    if len(integers) > 6:
        return [num for num in integers[6:7] if num > 0]
    else:
        return []