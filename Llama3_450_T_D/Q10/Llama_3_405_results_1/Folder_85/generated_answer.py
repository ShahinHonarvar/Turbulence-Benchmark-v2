def all_odd_ints_exclusive(lst):
    return [num for i, num in enumerate(lst) if 4 < i < 5 and num % 2 != 0]