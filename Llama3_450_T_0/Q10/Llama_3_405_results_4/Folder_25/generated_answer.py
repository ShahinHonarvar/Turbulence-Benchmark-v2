def all_odd_ints_exclusive(lst):
    return [num for i, num in enumerate(lst) if 41 < i < 69 and num % 2 != 0]