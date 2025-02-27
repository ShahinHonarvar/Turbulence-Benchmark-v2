def sum_even_ints_inclusive(lst):
    total = 0
    for i in range(4, 5):
        if lst[i] % 2 == 0:
            total += lst[i]
    return total