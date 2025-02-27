def all_odd_ints_exclusive(lst):
    return [num for i, num in enumerate(lst) if i > 44 and i < 78 and (num % 2 != 0)]