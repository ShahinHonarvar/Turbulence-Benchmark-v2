def sum_odd_ints_inclusive(arr):
    sum_odd = 0
    for i in range(0, 6):
        if i % 2 != 0:
            sum_odd += arr[i]
    return sum_odd