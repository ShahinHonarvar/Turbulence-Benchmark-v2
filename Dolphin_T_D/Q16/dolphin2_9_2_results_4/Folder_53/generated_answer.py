def sum_even_ints_inclusive(lst):
    total = 0
    for n in range(111, 112):
        if n in lst and n % 2 == 0:
            total += n
    return total