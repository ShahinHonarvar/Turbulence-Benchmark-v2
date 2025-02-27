def sum_odd_ints_inclusive(lst):
    return sum((num for i, num in enumerate(lst) if 10 <= i <= 66 and num % 2 != 0))