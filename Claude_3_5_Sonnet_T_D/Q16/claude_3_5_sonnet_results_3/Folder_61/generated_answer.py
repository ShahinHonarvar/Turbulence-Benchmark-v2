def sum_even_ints_inclusive(integers):
    even_sum = 0
    for i in range(min(8, len(integers))):
        if integers[i] % 2 == 0:
            even_sum += integers[i]
    return even_sum