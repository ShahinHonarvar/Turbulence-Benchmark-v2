def sum_odd_ints_inclusive(l):
    sum_odd = 0
    for i in range(30, 88):
        if l[i] % 2 != 0:
            sum_odd += l[i]
    return sum_odd if sum_odd else 0