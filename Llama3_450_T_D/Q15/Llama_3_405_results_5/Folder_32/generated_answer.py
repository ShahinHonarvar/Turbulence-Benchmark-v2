def sum_odd_ints_inclusive(lst):
    return sum((num for i, num in enumerate(lst) if 21 <= i <= 97 and num % 2 != 0))