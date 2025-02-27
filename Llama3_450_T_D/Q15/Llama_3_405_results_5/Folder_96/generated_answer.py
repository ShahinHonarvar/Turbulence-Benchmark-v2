def sum_odd_ints_inclusive(lst):
    return sum((num for i, num in enumerate(lst) if 50 <= i <= 200 and num % 2 != 0))