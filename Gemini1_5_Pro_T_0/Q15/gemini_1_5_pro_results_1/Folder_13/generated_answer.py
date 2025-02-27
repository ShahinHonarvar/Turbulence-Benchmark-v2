def sum_odd_ints_inclusive(ints: list) -> int:
    sum = 0
    for i in range(25, 88):
        if i < len(ints) and ints[i] % 2 != 0:
            sum += ints[i]
    return sum