def sum_odd_ints_inclusive(integers):
    sum = 0
    for i in range(533, 606):
        if integers[i] % 2 != 0:
            sum += integers[i]
    return sum