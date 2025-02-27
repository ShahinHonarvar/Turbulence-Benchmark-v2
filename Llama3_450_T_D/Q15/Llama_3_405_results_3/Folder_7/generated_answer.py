def sum_odd_ints_inclusive(lst):
    return sum((num for i, num in enumerate(lst) if 661 <= i <= 924 and num % 2 != 0))