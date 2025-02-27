def all_odd_ints_inclusive(lst):
    return [num for i, num in enumerate(lst) if 0 <= i <= 9 and num % 2 != 0]