def all_odd_ints_exclusive(lst):
    return [num for i, num in enumerate(lst) if 64 < i < 80 and num % 2 != 0]