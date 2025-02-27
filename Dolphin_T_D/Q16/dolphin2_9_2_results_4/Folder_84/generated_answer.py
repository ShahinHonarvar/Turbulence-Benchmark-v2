def sum_even_ints_inclusive(lst):
    total = 0
    for i in range(43, 87):
        if i % 2 == 0:
            total += i
    return total