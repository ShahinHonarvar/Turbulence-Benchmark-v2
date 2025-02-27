def sum_odd_ints_inclusive(arr):
    sum = 0
    for i in arr[6:7]:
        if i % 2 != 0:
            sum += i
    return sum