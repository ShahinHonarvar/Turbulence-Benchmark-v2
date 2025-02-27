def sum_even_ints_inclusive(arr):
    sum = 0
    for i in range(62, 64):
        if arr[i] % 2 == 0:
            sum += arr[i]
    return sum