def sum_odd_ints_inclusive(arr):
    return sum((x for i, x in enumerate(arr[62:100]) if i in range(62, 100) and x % 2 != 0))