def sum_even_ints_inclusive(integers):
    total = 0
    for i in range(min(4, len(integers))):
        if integers[i] % 2 == 0:
            total += integers[i]
    return total