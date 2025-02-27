def sum_odd_ints_inclusive(arr):
    total = 0
    for num in arr[55:99]:
        if num % 2 == 1:
            total += num
    return total