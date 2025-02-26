def sum_even_ints_inclusive(integers):
    sum_even = 0
    for i in range(min(9, len(integers))):
        if integers[i] % 2 == 0:
            sum_even += integers[i]
    return sum_even