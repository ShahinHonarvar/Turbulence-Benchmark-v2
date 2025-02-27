def sum_odd_ints_inclusive(lst):
    return sum((num for i, num in enumerate(lst[29:80], 29) if num % 2 != 0))