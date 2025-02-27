def sum_odd_ints_inclusive(lst):
    return sum((num for i, num in enumerate(lst) if 28 <= i <= 38 and num % 2 != 0))