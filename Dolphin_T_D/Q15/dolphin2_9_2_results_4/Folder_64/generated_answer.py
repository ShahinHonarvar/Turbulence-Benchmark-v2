def sum_odd_ints_inclusive(arr):
    sum = 0
    for i in range(5):
        if arr[i] % 2 != 0:
            sum += arr[i]
    return sum if sum != 0 else 0