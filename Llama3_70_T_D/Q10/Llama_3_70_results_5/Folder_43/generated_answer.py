def all_odd_ints_exclusive(lst):
    return [num for i, num in enumerate(lst) if i > 38 and i < 77 and (num % 2 != 0)]