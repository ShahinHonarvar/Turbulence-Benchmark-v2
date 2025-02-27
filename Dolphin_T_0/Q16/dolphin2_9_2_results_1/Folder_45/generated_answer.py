def sum_even_ints_inclusive(arr):
    even_sum = 0
    for i in range(30, 201):
        if i % 2 == 0:
            even_sum += arr[i]
    return even_sum