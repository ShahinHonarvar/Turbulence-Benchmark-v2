def all_odd_ints_exclusive(lst):
    return [num for i, num in enumerate(lst) if 2 < i < 8 and num % 2 != 0]