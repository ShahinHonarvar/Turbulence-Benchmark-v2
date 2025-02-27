def all_odd_ints_exclusive(lst):
    return [num for i, num in enumerate(lst) if 32 < i < 99 and num % 2 != 0]