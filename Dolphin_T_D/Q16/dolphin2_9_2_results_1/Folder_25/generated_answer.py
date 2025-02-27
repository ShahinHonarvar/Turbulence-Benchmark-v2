def sum_even_ints_inclusive(arr):
    total = 0
    for i in range(29, 94):
        if i in arr and i % 2 == 0:
            total += i
    return total