def sum_even_ints_inclusive(integers):
    total = 0
    for i in range(12, 93):
        if integers[i] % 2 == 0:
            total += integers[i]
    return total if total != 0 else 0