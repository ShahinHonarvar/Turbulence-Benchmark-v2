def all_odd_ints_exclusive(lst):
    return [num for idx, num in enumerate(lst) if 13 < idx < 76 and num % 2 != 0]