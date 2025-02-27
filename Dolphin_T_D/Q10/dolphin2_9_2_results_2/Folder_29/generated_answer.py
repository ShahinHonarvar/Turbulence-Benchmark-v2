def all_odd_ints_exclusive(ints):
    return [int for i, int in enumerate(ints) if i in range(50, 75) if int % 2 != 0]