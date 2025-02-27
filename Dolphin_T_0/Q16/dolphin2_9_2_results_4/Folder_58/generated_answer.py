def sum_even_ints_inclusive(arr):
    total = 0
    for i in range(209, 557):
        if i < len(arr) and arr[i] % 2 == 0:
            total += arr[i]
    return total