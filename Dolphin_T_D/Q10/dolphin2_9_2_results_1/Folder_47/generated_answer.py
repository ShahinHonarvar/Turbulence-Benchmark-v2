def all_odd_ints_exclusive(lst):
    return [value for index, value in enumerate(lst) if 64 < index < 80 and value % 2 == 1]