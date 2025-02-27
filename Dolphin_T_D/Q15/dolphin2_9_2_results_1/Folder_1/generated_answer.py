def sum_odd_ints_inclusive(arr):
    return sum((arr[i] for i in range(31, 73) if arr[i] % 2 != 0))