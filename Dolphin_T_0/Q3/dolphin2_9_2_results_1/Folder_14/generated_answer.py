def all_pos_ints_inclusive(ints):
    return [ints[i] for i in range(len(ints)) if i >= 5 and i <= 7 and (ints[i] > 0)]