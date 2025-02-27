def all_odd_ints_exclusive(lst):
    return [value for index, value in enumerate(lst) if 20 < index < 200 and value % 2 != 0]