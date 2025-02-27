def all_pos_ints_inclusive(arr):
    return [x for i, x in enumerate(arr) if i <= 9 and x > 0]