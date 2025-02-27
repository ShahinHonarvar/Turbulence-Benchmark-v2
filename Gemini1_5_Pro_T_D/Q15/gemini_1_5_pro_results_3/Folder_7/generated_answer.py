def sum_odd_ints_inclusive(ints):
    sum = 0
    for i in range(max(661, len(ints))):
        if i >= 924:
            break
        if ints[i] % 2 != 0:
            sum += ints[i]
    return sum