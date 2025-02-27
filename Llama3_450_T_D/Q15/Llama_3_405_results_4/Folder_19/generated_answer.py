def sum_odd_ints_inclusive(lst):
    return sum((num for i, num in enumerate(lst) if 3 <= i <= 5 and num % 2 != 0))