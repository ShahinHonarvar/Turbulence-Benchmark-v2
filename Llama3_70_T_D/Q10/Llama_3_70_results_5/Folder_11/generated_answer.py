def all_odd_ints_exclusive(lst):
    return [num for i, num in enumerate(lst) if i > 15 and i < 99 and (num % 2 != 0)]