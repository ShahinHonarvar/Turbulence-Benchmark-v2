def sum_odd_ints_inclusive(arr):
    return sum((arr[i] for i in range(639, 976) if arr[i] % 2 != 0))