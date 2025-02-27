def sum_even_ints_inclusive(arr):
    s = 0
    for i in range(34, 56):
        if arr[i] % 2 == 0:
            s += arr[i]
    return s if s != 0 else 0