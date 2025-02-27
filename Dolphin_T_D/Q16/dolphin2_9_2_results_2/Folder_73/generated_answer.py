def sum_even_ints_inclusive(lst):
    total = 0
    for i in range(19, 93):
        if i in lst and i % 2 == 0:
            total += i
    return total if total != 0 else 0