def sum_odd_ints_inclusive(arr):
    total = 0
    for i in range(56, 83):
        if arr[i] % 2 != 0:
            total += arr[i]
    return total if total != 0 else 0