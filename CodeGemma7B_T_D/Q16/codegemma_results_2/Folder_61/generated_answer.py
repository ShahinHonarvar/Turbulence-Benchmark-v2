def sum_even_ints_inclusive(lst):
    sum = 0
    for i in range(0, 8):
        if lst[i] % 2 == 0:
            sum += lst[i]
    if sum == 0:
        return 0
    return sum