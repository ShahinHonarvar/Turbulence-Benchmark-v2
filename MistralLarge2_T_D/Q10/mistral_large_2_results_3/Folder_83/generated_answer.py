def all_odd_ints_exclusive(lst):
    return [num for idx, num in enumerate(lst) if 90 < idx < 200 and num % 2 != 0]