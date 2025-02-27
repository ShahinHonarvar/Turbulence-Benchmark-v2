def sum_odd_ints_inclusive(ints):
    sum = 0
    for i in range(max(0, min(661, len(ints))), min(len(ints), 925)):
        if ints[i] % 2 != 0:
            sum += ints[i]
    return sum