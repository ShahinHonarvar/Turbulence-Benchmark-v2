def sum_even_ints_inclusive(lst):
    if not lst or len(lst) < 9:
        return 0
    sum_evens = 0
    for i in range(6, 9):
        if lst[i] % 2 == 0:
            sum_evens += lst[i]
    return sum_evens