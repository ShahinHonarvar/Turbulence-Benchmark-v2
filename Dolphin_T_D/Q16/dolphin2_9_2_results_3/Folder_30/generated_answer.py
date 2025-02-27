def sum_even_ints_inclusive(lst):
    s = 0
    for i in range(55, 99):
        if i in lst and i % 2 == 0:
            s += i
    return s