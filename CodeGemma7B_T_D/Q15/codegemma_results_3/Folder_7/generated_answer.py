def sum_odd_ints_inclusive(l):
    sum = 0
    for i in range(661, 925):
        if i % 2 == 1:
            sum += l[i]
    if sum == 0:
        return 0
    else:
        return sum