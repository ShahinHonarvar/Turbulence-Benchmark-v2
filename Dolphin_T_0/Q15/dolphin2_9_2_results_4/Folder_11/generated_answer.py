def sum_odd_ints_inclusive(l):
    result = 0
    for i in range(37, 52):
        if l[i] % 2 != 0:
            result += l[i]
    return result