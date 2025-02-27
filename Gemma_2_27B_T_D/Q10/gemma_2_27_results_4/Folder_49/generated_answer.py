def all_odd_ints_exclusive(ints):
    return [int for i, int in enumerate(ints) if i >= 80 and i < 200 and (int % 2 != 0)]