def all_odd_ints_exclusive(lst):
    return [num for i, num in enumerate(lst) if i > 369 and i < 983 and (num % 2 != 0)]