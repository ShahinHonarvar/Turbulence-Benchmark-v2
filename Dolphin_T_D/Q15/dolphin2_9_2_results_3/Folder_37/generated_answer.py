def sum_odd_ints_inclusive(integers):
    total = 0
    for index in range(1, 6):
        if integers[index] % 2 != 0:
            total += integers[index]
    return total if total != 0 else 0