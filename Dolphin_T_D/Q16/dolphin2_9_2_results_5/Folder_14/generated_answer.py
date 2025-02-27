def sum_even_ints_inclusive(arr):
    s = 0
    for i in arr[5:8]:
        if i % 2 == 0:
            s += i
    return s