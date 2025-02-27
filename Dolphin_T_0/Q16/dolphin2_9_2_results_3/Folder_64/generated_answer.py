def sum_even_ints_inclusive(arr):
    if not isinstance(arr, list) or len(arr) < 5:
        return 0
    s = 0
    for i in range(5):
        if arr[i] % 2 == 0:
            s += arr[i]
    return s