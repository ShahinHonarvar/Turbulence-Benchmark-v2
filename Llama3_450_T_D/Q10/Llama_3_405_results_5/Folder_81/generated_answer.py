def all_odd_ints_exclusive(lst):
    return [num for i, num in enumerate(lst) if 10 < i < 11 and num % 2 != 0]