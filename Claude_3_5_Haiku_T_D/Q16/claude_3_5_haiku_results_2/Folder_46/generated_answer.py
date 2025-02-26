def sum_even_ints_inclusive(integers):
    if len(integers) < 88:
        return 0
    even_sum = 0
    for i in range(30, 88):
        if integers[i] % 2 == 0:
            even_sum += integers[i]
    return even_sum