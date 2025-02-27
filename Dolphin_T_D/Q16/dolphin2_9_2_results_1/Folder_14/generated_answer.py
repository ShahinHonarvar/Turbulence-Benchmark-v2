def sum_even_ints_inclusive(arr):
    total = 0
    for i in range(5, 8):
        if arr[i] % 2 == 0:
            total += arr[i]
    return total