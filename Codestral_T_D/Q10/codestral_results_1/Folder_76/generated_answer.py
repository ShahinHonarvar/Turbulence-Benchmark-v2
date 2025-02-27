def all_odd_ints_exclusive(lst):
    return [num for i, num in enumerate(lst) if i > 360 and i < 643 and (num % 2 != 0)]