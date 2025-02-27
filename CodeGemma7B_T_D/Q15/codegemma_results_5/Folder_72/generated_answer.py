def sum_odd_ints_inclusive(arr):
    s = 0
    for i in range(29, 52):
        if arr[i] % 2 != 0:
            s += arr[i]
    return s if s else 0