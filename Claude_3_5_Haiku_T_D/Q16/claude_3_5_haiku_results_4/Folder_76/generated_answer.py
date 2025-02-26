def sum_even_ints_inclusive(integers):
    if len(integers) < 988:
        return 0
    even_sum = 0
    for i in range(686, 988):
        if integers[i] % 2 == 0:
            even_sum += integers[i]
    return even_sum