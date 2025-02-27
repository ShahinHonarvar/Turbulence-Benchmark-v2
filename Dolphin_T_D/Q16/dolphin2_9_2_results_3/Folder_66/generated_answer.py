def sum_even_ints_inclusive(arr):
    result = 0
    for i in range(50, 55):
        if i < len(arr) and arr[i] % 2 == 0:
            result += arr[i]
    return result