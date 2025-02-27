def all_odd_ints_exclusive(lst):
    return [num for i, num in enumerate(lst) if i > 49 and i < 74 and (num % 2 != 0)]