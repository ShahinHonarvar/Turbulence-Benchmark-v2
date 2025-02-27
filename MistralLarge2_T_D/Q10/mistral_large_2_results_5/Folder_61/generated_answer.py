def all_odd_ints_exclusive(lst):
    return [num for i, num in enumerate(lst) if num % 2 != 0 and 0 < i < 7]