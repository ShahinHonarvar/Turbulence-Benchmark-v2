def all_odd_ints_exclusive(lst):
    return [num for i, num in enumerate(lst) if i > 389 and i < 748 and (num % 2 != 0)]