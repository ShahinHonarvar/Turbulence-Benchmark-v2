def sum_odd_ints_inclusive(lst):
    return sum((num for i, num in enumerate(lst) if i <= 7 and num % 2 != 0))