def sum_even_ints_inclusive(arr):
    even_sum = 0
    for i in range(34, 56):
        if arr[i] % 2 == 0:
            even_sum += arr[i]
    return even_sum if even_sum != 0 else 0