def sum_even_ints_inclusive(lst):
    s = 0
    for i in range(62, 79):
        if i < len(lst):
            if lst[i] % 2 == 0:
                s += lst[i]
    return s