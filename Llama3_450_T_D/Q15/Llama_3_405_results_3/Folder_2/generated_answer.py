def sum_odd_ints_inclusive(lst):
    return sum((num for idx, num in enumerate(lst) if 15 <= idx <= 39 and num % 2 != 0))