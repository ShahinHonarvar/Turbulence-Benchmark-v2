def all_odd_ints_inclusive(lst):
    return [num for i, num in enumerate(lst) if i <= 9 and num % 2 != 0]