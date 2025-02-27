def all_odd_ints_exclusive(lst):
    return [num for i, num in enumerate(lst) if 13 < i < 70 and num % 2 != 0]