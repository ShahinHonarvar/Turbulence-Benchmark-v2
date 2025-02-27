def all_odd_ints_inclusive(lst):
    return [num for i, num in enumerate(lst) if 14 <= i <= 64 and num % 2 != 0]