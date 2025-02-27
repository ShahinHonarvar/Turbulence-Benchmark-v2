def sum_even_ints_inclusive(arr):
    sum_even = 0
    for i in range(23, 24):
        if arr[i] % 2 == 0:
            sum_even += arr[i]
    return sum_even