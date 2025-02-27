def sum_odd_ints_inclusive(arr):
    return sum((val for i, val in enumerate(arr[30:49]) if i % 2 != 0))