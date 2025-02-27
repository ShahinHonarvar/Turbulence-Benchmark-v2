def sum_even_ints_inclusive(lst):
    total_sum = 0
    for i in range(29, 52):
        if lst[i] % 2 == 0:
            total_sum += lst[i]
    return total_sum