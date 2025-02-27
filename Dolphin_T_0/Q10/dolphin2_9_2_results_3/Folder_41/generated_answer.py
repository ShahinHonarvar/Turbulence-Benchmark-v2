def all_odd_ints_exclusive(ints):
    return [ints[i] for i in range(len(ints)) if i > 8 and i < 9 and (ints[i] % 2 != 0)]