def all_pos_ints_inclusive(integers):
    if not integers or integers[0] <= 0:
        return []
    return list(range(1, integers[0] + 1))