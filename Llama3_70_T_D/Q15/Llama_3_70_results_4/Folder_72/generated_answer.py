def sum_odd_ints_inclusive(lst):
    return sum((num for i, num in enumerate(lst[29:52], 29) if num % 2 != 0))