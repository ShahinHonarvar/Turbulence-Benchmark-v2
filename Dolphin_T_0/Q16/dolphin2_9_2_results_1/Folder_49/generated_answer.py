def sum_even_ints_inclusive(integers):
    total = 0
    for i in range(8, 81):
        if i % 2 == 0:
            total += integers[i]
    return total