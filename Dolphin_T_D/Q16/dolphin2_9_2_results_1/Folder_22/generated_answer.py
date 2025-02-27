def sum_even_ints_inclusive(arr):
    even_sum = 0
    for i in range(40, 42):
        if i < len(arr) and arr[i] % 2 == 0:
            even_sum += arr[i]
    return even_sum