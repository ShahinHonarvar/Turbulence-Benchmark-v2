def all_odd_ints_exclusive(lst):
    return [num for i, num in enumerate(lst) if 19 < i < 94 and num % 2 != 0]