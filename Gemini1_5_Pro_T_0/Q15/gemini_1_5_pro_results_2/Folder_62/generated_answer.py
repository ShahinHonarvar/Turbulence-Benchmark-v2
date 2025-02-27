def sum_odd_ints_inclusive(ints: list) -> int:
    sum = 0
    for i in range(max(91, 0), min(len(ints), 100)):
        if ints[i] % 2 != 0:
            sum += ints[i]
    return sum