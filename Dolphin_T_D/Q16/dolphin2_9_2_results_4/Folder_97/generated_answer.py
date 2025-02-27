def sum_even_ints_inclusive(l):
    sum_even_ints = 0
    for i in range(40, 81):
        if i < len(l) and l[i] % 2 == 0:
            sum_even_ints += l[i]
    return sum_even_ints if sum_even_ints != 0 else 0