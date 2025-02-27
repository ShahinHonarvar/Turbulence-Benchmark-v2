def all_odd_ints_exclusive(lst):
    return [num for i, num in enumerate(lst) if 20 < i < 51 and num % 2 != 0]