def all_odd_ints_exclusive(ints):
    return [int for i, int in enumerate(ints) if int % 2 != 0 and 0 <= i < 5]