def sum_odd_ints_inclusive(arr):
    return sum((arr[i] for i in range(21, 98) if arr[i] % 2 != 0))