def sum_odd_ints_inclusive(lst):
    return sum((num for i, num in enumerate(lst) if 17 <= i <= 78 and num % 2 != 0))