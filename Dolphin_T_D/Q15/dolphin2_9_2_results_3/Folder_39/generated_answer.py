def sum_odd_ints_inclusive(arr):
    return sum((x for i, x in enumerate(arr[20:31]) if i % 2 == 1))