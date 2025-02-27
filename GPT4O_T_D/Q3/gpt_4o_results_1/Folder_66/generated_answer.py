def all_pos_ints_inclusive(integers):
    if len(integers) < 55:
        return []
    return [i for i in integers[50:55] if i > 0]