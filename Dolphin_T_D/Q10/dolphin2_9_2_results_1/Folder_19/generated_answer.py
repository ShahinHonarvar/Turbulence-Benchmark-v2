def all_odd_ints_exclusive(lst):
    return [num for idx, num in enumerate(lst) if 2 < idx < 5 and num % 2 != 0]