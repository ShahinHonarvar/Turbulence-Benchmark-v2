def sum_even_ints_inclusive(lst):
    total = 0
    for i in range(90, 201):
        if i % 2 == 0 and i in lst:
            total += i
    return total