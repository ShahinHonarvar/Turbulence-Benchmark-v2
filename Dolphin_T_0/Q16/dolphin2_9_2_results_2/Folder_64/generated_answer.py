def sum_even_ints_inclusive(arr):
    return sum((arr[i] for i in range(5) if arr[i] % 2 == 0))