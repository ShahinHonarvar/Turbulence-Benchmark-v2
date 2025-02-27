def all_odd_ints_inclusive(lst):
    return [num for i, num in enumerate(lst) if 20 <= i <= 200 and num % 2 != 0]