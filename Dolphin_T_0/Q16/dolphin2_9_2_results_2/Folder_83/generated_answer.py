def sum_even_ints_inclusive(lst):
    s = 0
    for i in range(90, 201):
        if i % 2 == 0:
            s += lst[i]
    return s