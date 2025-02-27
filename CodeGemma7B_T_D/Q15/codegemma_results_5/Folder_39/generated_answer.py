def sum_odd_ints_inclusive(l):
    sum = 0
    for i in range(20, 31):
        if i % 2 != 0:
            sum += l[i]
    return sum