def sum_even_ints_inclusive(lst):
    total = 0
    for i in range(12, 93):
        if i % 2 == 0:
            total += lst[i]
    return total