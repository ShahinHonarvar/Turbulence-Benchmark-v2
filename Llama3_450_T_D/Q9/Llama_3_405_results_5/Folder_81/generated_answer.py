def all_odd_ints_inclusive(lst):
    return [num for i, num in enumerate(lst) if 10 <= i <= 100 and num % 2 != 0]