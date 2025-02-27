def all_odd_ints_exclusive(ints):
    return [int for index, int in enumerate(ints) if 2 <= index < 8 and int % 2 != 0]