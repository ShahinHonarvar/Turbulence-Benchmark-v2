def all_odd_ints_exclusive(lst):
    return [num for idx, num in enumerate(lst[14:76]) if num % 2 != 0]