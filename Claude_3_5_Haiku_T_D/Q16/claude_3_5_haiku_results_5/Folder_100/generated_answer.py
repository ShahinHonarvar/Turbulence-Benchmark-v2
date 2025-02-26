def sum_even_ints_inclusive(integers):
    if len(integers) < 69:
        return 0
    even_sum = 0
    for index in range(42, 69):
        if integers[index] % 2 == 0:
            even_sum += integers[index]
    return even_sum