def all_pos_ints_inclusive(integers):
    if len(integers) > 4:
        return [num for num in integers[4:5] if num > 0]
    else:
        return []