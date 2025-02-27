def sum_odd_ints_inclusive(arr):
    odd_sum = 0
    for i in range(0, len(arr)):
        if arr[i] % 2 == 1:
            odd_sum += arr[i]
    return odd_sum if odd_sum > 0 else 0