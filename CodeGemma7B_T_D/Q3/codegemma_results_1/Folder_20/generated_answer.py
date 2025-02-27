def all_pos_ints_inclusive(lst):
    for i in range(56, 67):
        if lst[i] > 0:
            return lst[i:i + 1]
    return []