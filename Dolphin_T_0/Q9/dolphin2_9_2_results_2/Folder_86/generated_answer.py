def all_odd_ints_inclusive(lst):
    return [num for i, num in enumerate(lst) if 31 <= i <= 34 and num % 2 != 0]