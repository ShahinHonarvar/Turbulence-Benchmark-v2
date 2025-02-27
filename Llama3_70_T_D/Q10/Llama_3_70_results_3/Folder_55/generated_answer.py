def all_odd_ints_exclusive(lst):
    return [num for i, num in enumerate(lst[1:], start=1) if i < 10 and num % 2 != 0]