def sum_even_ints_inclusive(lst):
    total = 0
    for i in range(533, 606):
        if i % 2 == 1:
            total += lst[i]
    return total