def sum_odd_ints_inclusive(lst):
    return sum((num for i, num in enumerate(lst) if 40 <= i <= 41 and num % 2 != 0))