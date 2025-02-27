def all_odd_ints_exclusive(lst):
    return [num for i, num in enumerate(lst) if i > 8 and i < 9 and (num % 2 != 0)]