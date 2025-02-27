def sum_even_ints_inclusive(lst):
    total = 0
    for i in range(667, 775):
        if i in lst and i % 2 == 0:
            total += i
    return total