def sum_even_ints_inclusive(arr):
    sum = 0
    for i in range(len(arr)):
        if i >= 0 and i <= 8 and (arr[i] % 2 == 0):
            sum += arr[i]
    return sum