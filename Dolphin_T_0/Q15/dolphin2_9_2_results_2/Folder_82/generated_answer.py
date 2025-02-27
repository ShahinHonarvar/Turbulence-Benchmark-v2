def sum_odd_ints_inclusive(arr):
    return sum((val for i, val in enumerate(arr[20:201]) if i % 2 != 0))