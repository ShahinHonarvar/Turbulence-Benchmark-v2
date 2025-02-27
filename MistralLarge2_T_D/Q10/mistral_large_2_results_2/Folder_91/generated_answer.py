def all_odd_ints_exclusive(lst):
    return [num for idx, num in enumerate(lst) if idx > 0 and idx < 5 and (num % 2 != 0)]