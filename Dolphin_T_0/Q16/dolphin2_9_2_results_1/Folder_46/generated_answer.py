def sum_even_ints_inclusive(lst):
    total = 0
    for i in range(30, 88):
        if i % 2 == 0:
            total += lst[i]
    return total