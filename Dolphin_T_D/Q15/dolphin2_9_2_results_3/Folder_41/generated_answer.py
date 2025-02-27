def sum_odd_ints_inclusive(arr):
    return sum((val for index, val in enumerate(arr[6:7]) if val % 2 != 0))