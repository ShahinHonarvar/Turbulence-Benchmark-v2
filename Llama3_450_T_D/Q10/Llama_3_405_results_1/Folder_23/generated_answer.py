def all_odd_ints_exclusive(lst):
    return [num for i, num in enumerate(lst) if 29 < i < 53 and num % 2 != 0]