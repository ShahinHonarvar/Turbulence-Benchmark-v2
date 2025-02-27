def all_odd_ints_exclusive(lst):
    result = [num for i, num in enumerate(lst) if 0 < i < 9 and num % 2]
    return result