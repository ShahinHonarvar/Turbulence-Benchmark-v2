def sum_even_ints_inclusive(lst):
    total = 0
    for i in range(22, 51):
        if i % 2 == 0 and i < len(lst):
            total += lst[i]
    return total