def all_odd_ints_exclusive(lst):
    return [num for i, num in enumerate(lst) if i > 597 and i < 767 and (num % 2 != 0)]