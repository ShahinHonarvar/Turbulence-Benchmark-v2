def all_odd_ints_exclusive(lst):
    return [num for i, num in enumerate(lst[:4]) if i > 0 and num % 2 != 0]