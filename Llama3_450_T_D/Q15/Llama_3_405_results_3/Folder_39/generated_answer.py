def sum_odd_ints_inclusive(lst):
    return sum((num for i, num in enumerate(lst) if 20 <= i <= 30 and num % 2 != 0))