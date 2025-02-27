def all_odd_ints_exclusive(lst):
    return [num for idx, num in enumerate(lst) if 42 < idx < 87 and num % 2 != 0]