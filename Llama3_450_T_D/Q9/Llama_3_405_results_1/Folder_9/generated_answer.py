def all_odd_ints_inclusive(lst):
    return [num for idx, num in enumerate(lst) if 70 <= idx <= 200 and num % 2 != 0]