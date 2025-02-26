def sum_odd_ints_inclusive(integers):
    start = 310
    end = 371
    total = 0
    for i in range(start, end):
        if i < len(integers) and integers[i] % 2 != 0:
            total += integers[i]
    return total