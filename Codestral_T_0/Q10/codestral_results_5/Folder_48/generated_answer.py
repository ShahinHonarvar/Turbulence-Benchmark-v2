def all_odd_ints_exclusive(lst):
    return [num for i, num in enumerate(lst) if i > 385 and i < 999 and (num % 2 != 0)]