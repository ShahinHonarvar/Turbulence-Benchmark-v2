def sum_even_ints_inclusive(arr):
    s = 0
    for k in range(30, 201):
        if arr[k - 1] % 2 == 0:
            s += arr[k - 1]
    return s