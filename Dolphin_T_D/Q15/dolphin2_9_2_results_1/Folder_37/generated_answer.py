def sum_odd_ints_inclusive(arr):
    return sum((val for i, val in enumerate(arr[1:6]) if val % 2 != 0))